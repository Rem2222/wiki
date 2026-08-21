#!/usr/bin/env python3
"""
Zvec Wiki MCP Server (read-only).

Provides a native MCP tool `zvec_wiki_search` for hybrid (vector+FTS) semantic
search over the Markdown wiki (~/Documents/wiki/) via Zvec.

Reuses the exact search logic + index from zvec_search.py (bge-m3 via Ollama,
hybrid vector+FTS, RRF rerank). No OpenAI key needed.

Run:  /root/.zvec-venv/bin/python zvec_mcp_server.py
"""
import sys
import json

sys.path.insert(0, "/root/.zvec-venv/lib/python3.12/site-packages")

import zvec
from zvec.extension import HTTPDenseEmbedding, RrfReRanker
from zvec.model.param import FtsQueryParam, HnswQueryParam
from zvec.model.param.query import Query, Fts

from fastmcp import FastMCP

INDEX_DIR = "/root/.zvec-wiki/index"
EMBED_URL = "http://localhost:11434"
EMBED_MODEL = "bge-m3"

mcp = FastMCP("zvec-wiki")


def _search(query: str, topk: int = 10, page_only: bool = False) -> list:
    zvec.init(log_type=zvec.LogType.CONSOLE, log_level=zvec.LogLevel.ERROR)
    coll = zvec.open(INDEX_DIR, zvec.CollectionOption(read_only=True, enable_mmap=True))
    emb = HTTPDenseEmbedding(base_url=EMBED_URL, model=EMBED_MODEL)
    vec_query = Query(field_name="embedding", vector=emb.embed(query),
                      param=HnswQueryParam(ef=100))
    fts_query = Query(field_name="content", fts=Fts(match_string=query),
                      param=FtsQueryParam(default_operator="OR"))
    res = coll.query(queries=[vec_query, fts_query], topk=topk * 3,
                     reranker=RrfReRanker(),
                     output_fields=["page", "category", "title", "content"])
    results = []
    seen = set()
    for d in res:
        f = d.fields or {}
        page = f.get("page", d.id)
        item = {
            "page": page,
            "category": f.get("category", ""),
            "title": f.get("title", ""),
            "score": round(float(d.score), 4) if d.score is not None else None,
            "snippet": (f.get("content") or "")[:300],
        }
        if page_only:
            if page in seen:
                continue
            seen.add(page)
            item.pop("snippet", None)
        results.append(item)
        if len(results) >= topk:
            break
    return results


@mcp.tool()
def zvec_wiki_search(query: str, topk: int = 10, page_only: bool = False) -> str:
    """Hybrid (vector bge-m3 + FTS) semantic search over the Markdown wiki (~/Documents/wiki/).

    Args:
        query: natural-language search query (Russian/English OK).
        topk: max results to return (default 10).
        page_only: if True, dedupe to one result per page (no snippets).

    Returns:
        JSON list of {page, category, title, score, snippet} ranked by relevance.
    """
    try:
        results = _search(query, topk=topk, page_only=page_only)
        return json.dumps(results, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)})


if __name__ == "__main__":
    mcp.run()