# Hindsight MM scoping + zvec MCP/wiki-write (2026-08-21)

Condensed, verified learnings from the MUL-874/Hindsight + MUL-891 (zvec) session.

## 1. Hindsight mental models: tags-scoping pitfall (was empty)

**Root cause of "MM exists but content = 'информация отсутствует'":** when you set
non-empty `tags` on a mental model, refresh does a **scoped-by-tags** retrieval — it
only reads memory_units carrying those tags. In bank `hermes`, **~30212 of 30244
memory_units have empty tags `{}`** (only ~32 carry `session:*` tags from backfill).
A tag-scoped MM finds nothing → content is generated as "no info found".

**Fix:** leave `tags=[]` on MMs that must reflect the whole bank. Empty tag scope =
sees everything. Confirmed 21.08: after clearing tags, the "Текущий фокус" MM
populated correctly (project statuses, decisions); with tags it was empty.

**Verified usage chain (Python client, async):**
```python
from hindsight_client import Hindsight
import asyncio
c = Hindsight(base_url="http://127.0.0.1:8888", api_key="hs-...")
# create (sync method) — returns mental_model_id
r = c.create_mental_model(bank_id="hermes", name="...",
    source_query="<stable question>",
    tags=[],  # IMPORTANT: empty, else scoped & empty
    trigger={"refresh_after_consolidation": True})
# refresh (async) — queues LLM refresh; content fills in after a minute or two
asyncio.run(c.mental_models.refresh_mental_model(bank_id="hermes",
    mental_model_id=r.mental_model_id))
# close(); don't await a None
```
- `create_mental_model` is sync and returns a **response object** (not dict) — read
  `.mental_model_id` / `.operation_id`, not `.get()`.
- refresh is **queued** (returns `status='queued'`), LLM generation takes ~1-3 min.
- `dry_run_refresh` / long embed via Ollama can exceed default tool timeout — run in
  background or with raised timeout.
- Verify via SQL: `docker exec hindsight-db psql -U hindsight_user -d hindsight_db \
  -c "SELECT name, length(content) FROM mental_models;"` — length>0 = populated.

## 2. zvec MCP server (read-only) + wiki-write writer

Goal: native wiki semantic search for Hermes (was shell CLI `zvec-wiki`) + a single
consistent writer so every agent writes valid Obsidian frontmatter.

### zvec MCP server (FastMCP, stdio, no OpenAI key)
- Location: `/root/.zvec-mcp/zvec_mcp_server.py`, launcher `/usr/local/bin/zvec-mcp`
  (chmod +x; uses `/root/.zvec-venv/bin/python` where fastmcp 3.4.7 + zvec installed).
- One tool `zvec_wiki_search(query, topk, page_only)` reusing zvec_search.py logic:
  hybrid vector (bge-m3 via Ollama :11434) + FTS, RRF rerank, read-only.
- Register in Hermes: `echo y | hermes mcp add zvec --command /usr/local/bin/zvec-mcp`
  (client already registered server `gbrain`/`context7` etc.). Verify:
  `hermes mcp test zvec` → Connected, 1 tool.
- To smoke-test raw JSON-RPC by hand, must send `notifications/initialized` + a small
  sleep after `initialize` before `tools/call`, or the call returns nothing.

### Why NOT the official zvec-mcp-server
`zvec-ai/zvec-mcp-server` (⭐7) requires an OpenAI key for embedding and is full-CRUD
create/index/delete oriented — wrong for our read-only search over an existing
bge-m3 index. Our wiki's source of truth is the `.md` files; zvec is only a
projection/index, so full CRUD on the index is pointless (rebuild would wipe edits).

### wiki-write (single writer)
- Location: `/root/.hermes/scripts/wiki-write.py`, launcher `/usr/local/bin/wiki-write`
  (chmod +x, else "Permission denied").
- Args: `--title --dir --description --tags --related --body<file> [--update <path>]`.
- Generates frontmatter per canonical standard (`description`/`tags:[..]`/`related`),
  writes `<WIKI>/{dir}/{slug}.md`, git add+commit+push, then background-launches
  zvec index rebuild via `subprocess.Popen(..., start_new_session=True)`.
- **Slug is transliterated to latin** (Cyrillic filenames are bad for Obsidian/URLs).
- `--update` patches existing page keeping related links.
- **Rebuild is not incremental and slow** (full re-embed ~1263 chunks ≈ 13 min via
  Ollama; single `build_index.py --force` run must NOT be awaited inline or the
  tool times out at 600s). Keep it fire-and-forget; check
  `/root/.zvec-wiki/rebuild.log`.
- Allowed dirs: tech, tools, projects, concepts, events, articles, books, misc,
  videos, wiki/tech, wiki/projects, wiki/concepts, wiki/people, wiki/books, wiki/misc.

## 3. Mental models / knowledge pages are curated, not auto
MM/KP are filled **explicitly** (MCP `create_mental_model` / `create_knowledge_page`),
auto-growing only via `trigger_refresh_after_consolidation` / refresh_cron.
background_review whitelist (memory+skills only) cannot call create_mental_model —
so night-creation belongs in the Night Routine (Shag 11), not the review fork.
Zero MM at the start is normal until someone creates them.