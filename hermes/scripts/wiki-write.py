#!/usr/bin/env python3
"""
wiki-write — единая точка записи в вики Rem (~/Documents/wiki/, Obsidian).

Все агенты (Hermes, Hermes Helper, Multica-автопилоты) пишут в вики ТОЛЬКО через
этот скрипт, чтобы frontmatter/заголовки/пути всегда были валидны для Obsidian.

Формат frontmatter (канон из memory-wiki-workflow/references/wiki-frontmatter-standard.md):
    description (обяз), tags: [..,..] (обяз, массив lowercase), related: [[..]] (опц)

Usage:
  wiki-write --title "Название" --dir tech \
             --description "что это (2-3 предложения)" \
             --tags "poc,mcp,vector-db" \
             [--related "[[tech/zvec]] [[tools/...]]"] \
             --body /tmp/body.md              # тело страницы (markdown)
             [--update path/to/existing.md]    # обновить существующую страницу

После записи: git add+commit+push + auto-rebuild zvec-индекса.
"""
import argparse
import os
import re
import subprocess
import sys

WIKI = "/root/Documents/wiki"
ALLOWED_DIRS = {
    "tech", "tools", "projects", "concepts", "events", "articles",
    "books", "misc", "videos", "wiki/tech", "wiki/projects", "wiki/concepts",
    "wiki/people", "wiki/books", "wiki/misc",
}
BUILD_INDEX = "/root/.zvec-wiki/build_index.py"
ZBUILD_PY = "/root/.zvec-venv/bin/python"


def slugify(title: str) -> str:
    # транслитерация кириллицы → латиница для имён файлов
    translit = {
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e",
        "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
        "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
        "ф": "f", "х": "h", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "sch",
        "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ж": "zh",
        "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n",
        "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f",
        "х": "h", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "sch", "ы": "y",
        "ю": "yu", "я": "ya",
    }
    s = title.strip().lower()
    s = "".join(translit.get(ch, ch) for ch in s)
    s = re.sub(r"[^a-z0-9\- ]", "", s)
    s = s.replace(" ", "-")
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s


def build_frontmatter(description, tags, related) -> str:
    fm = ["---", f"description: \"{description}\"", f"tags: [{tags}]"]
    if related:
        fm.append(f"related: {related}")
    fm.append("---")
    return "\n".join(fm) + "\n"


def read_or_empty(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--dir", required=True, help="category dir (tech/tools/...); or path alias")
    ap.add_argument("--description", required=True)
    ap.add_argument("--tags", required=True, help="comma-separated, lowercase")
    ap.add_argument("--related", default="", help="[[wikilinks]] space-separated")
    ap.add_argument("--body", default="", help="path to body markdown file")
    ap.add_argument("--update", default="", help="update existing page path")
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--no-rebuild", action="store_true")
    args = ap.parse_args()

    if args.dir not in ALLOWED_DIRS:
        sys.stderr.write(f"ERROR: dir '{args.dir}' не из разрешённых: {sorted(ALLOWED_DIRS)}\n")
        return 2

    # destination
    if args.update:
        full = args.update if args.update.startswith("/") else os.path.join(WIKI, args.update)
        if not full.startswith(WIKI):
            sys.stderr.write("ERROR: path вне вики\n")
            return 2
    else:
        fname = slugify(args.title) + ".md"
        full = os.path.join(WIKI, args.dir, fname)

    body = read_or_empty(args.body)
    front = build_frontmatter(args.description, args.tags, args.related)
    content = front + "\n# " + args.title + "\n\n" + body.strip() + "\n"

    os.makedirs(os.path.dirname(full), exist_ok=True)
    changed = True
    if os.path.exists(full) and read_or_empty(full) == content:
        changed = False
        print(f"no-change: {full}")

    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    rel = os.path.relpath(full, WIKI)
    print(f"write: {rel} ({len(content)} chars, {'new' if not args.update else 'update'})")

    # git commit + push
    if not args.no_push:
        subprocess.run(["git", "add", "-A"], cwd=WIKI, check=True)
        subprocess.run(["git", "commit", "-m", f"wiki: {args.title}"], cwd=WIKI,
                       capture_output=True)
        subprocess.run(["git", "pull", "--rebase"], cwd=WIKI, capture_output=True)
        p = subprocess.run(["git", "push", "origin", "master"], cwd=WIKI,
                           capture_output=True)
        if p.returncode != 0:
            print("git push:", (p.stderr or p.stdout).decode()[-200:])

    # auto-rebuild zvec index — fire-and-forget (не блокирует запись, не падает
    # по таймауту; полный пере-эмбеддинг индекса -> фоновая задача)
    if not args.no_rebuild and os.path.exists(BUILD_INDEX):
        log = open("/root/.zvec-wiki/rebuild.log", "a", encoding="utf-8")
        subprocess.Popen(
            [ZBUILD_PY, BUILD_INDEX],
            stdout=log, stderr=subprocess.STDOUT, start_new_session=True,
        )
        print("zvec index rebuild: launched in background (see /root/.zvec-wiki/rebuild.log)")

    return 0


if __name__ == "__main__":
    sys.exit(main())