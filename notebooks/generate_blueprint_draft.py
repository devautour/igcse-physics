"""Generate a blueprint draft spanning all 8 units.

Reads the nav structure from mkdocs.yml and, for each page, extracts:
  - Markdown headings (#, ##, ...)
  - explicitly-marked content descriptors, i.e. admonition titles
    (`!!! type "Definition: xxx"`, `!!! type "Worked Example (calculation)"`, ...)

Nothing here interprets or classifies the descriptors -- it just pulls out
titles that are already explicitly marked up in the source. A few things are
deliberately dropped as noise rather than content:
  - the top "Unit N" nav wrapper -- its child ("N - Title") already carries
    the heading, so the wrapper is just a redundant extra level
  - unit overview pages (`index.md`) -- these just restate the nav structure
    and a blurb, nothing spec-relevant
  - each page's own title heading -- it just repeats the nav heading printed
    for that page, so keeping it would duplicate the section name
  - subsections *within* a "Core practical" heading (Aim, Variables,
    Equipment, Method, ...) -- these are a fixed template repeated on every
    core-practical page, not distinguishing content. The "Core practical"
    heading itself is kept as a marker.

The nav hierarchy (unit number, section, subsection, page) is rendered as
Markdown headings. Everything below page level -- the page's own headings and
content descriptors -- is rendered as indented bullets, normalized to the
page's local nesting (not raw `#` count), since that can nest deeper than
heading levels allow.

Re-run any time docs/ changes; expect to adapt the extraction/formatting as
the content taxonomy is refined.

Usage:
    conda run -n igcse-physics python notebooks/generate_blueprint_draft.py
"""

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MKDOCS_YML = ROOT / "mkdocs.yml"
DOCS = ROOT / "docs"
OUTPUT = ROOT / "blueprint drafts" / "blueprint-draft.md"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
ADMONITION_RE = re.compile(r'^\s*!!!\s+\S+\s+"([^"]*)"')
CORE_PRACTICAL_RE = re.compile(r"core practical", re.IGNORECASE)

MAX_HEADING_LEVEL = 6
INDENT = "  "


def load_nav():
    """Pull just the `nav:` block out of mkdocs.yml and parse it with yaml.

    Avoided yaml.safe_load on the whole file because markdown_extensions
    uses `!!python/name:...` tags that safe_load can't handle.
    """
    text = MKDOCS_YML.read_text(encoding="utf-8")
    nav_text = text.split("\nnav:\n", 1)[1].split("\nmarkdown_extensions:", 1)[0]
    return yaml.safe_load("nav:\n" + nav_text)["nav"]


def walk_nav(nav, depth=1):
    """Flatten the nav tree into (depth, title_or_None, target) tuples.

    `target` is a .md path for leaf pages, or None for group nodes (whose
    children follow immediately after in the flattened list).
    """
    items = []
    for entry in nav:
        if isinstance(entry, str):
            items.append((depth, None, entry))
        elif isinstance(entry, dict):
            for title, value in entry.items():
                title = title.strip()
                if isinstance(value, str):
                    items.append((depth, title, value))
                else:
                    items.append((depth, title, None))
                    items.extend(walk_nav(value, depth + 1))
    return items


def extract_page_lines(md_path):
    """Return indented bullet lines for a page's headings + content
    descriptors, in document order. The page's own title heading (the first
    one in the file) is skipped -- see module docstring.

    Heading depth is normalized to the page's own local nesting (via a
    stack), not the raw `#` count, so it stays correct regardless of how
    deep it nests.
    """
    lines = []
    stack = []
    current_indent = 0
    suppress_until_depth = None  # set while inside a "core practical" subtree
    seen_first_heading = False

    for line in md_path.read_text(encoding="utf-8").splitlines():
        heading_match = HEADING_RE.match(line)
        if heading_match:
            if not seen_first_heading:
                seen_first_heading = True
                continue  # page's own title heading -- duplicates the nav heading above it

            orig_level = len(heading_match.group(1))
            text = heading_match.group(2).strip()

            while stack and stack[-1] >= orig_level:
                stack.pop()
            stack.append(orig_level)
            local_depth = len(stack)

            if suppress_until_depth is not None and local_depth > suppress_until_depth:
                continue  # still inside a suppressed core-practical subtree

            suppress_until_depth = None

            current_indent = local_depth - 1
            lines.append(f"{INDENT * current_indent}- {text}")

            if CORE_PRACTICAL_RE.search(text):
                suppress_until_depth = local_depth
            continue

        if suppress_until_depth is not None:
            continue

        admonition_match = ADMONITION_RE.match(line)
        if admonition_match:
            lines.append(f"{INDENT * (current_indent + 1)}- {admonition_match.group(1).strip()}")

    return lines


def main():
    nav = load_nav()
    out = [
        "# Blueprint Draft",
        "",
        "Auto-generated from `mkdocs.yml` nav and `docs/` headings + explicitly "
        "marked content descriptors (admonition titles). Unit overview pages, "
        "page title headings and core-practical subsections are skipped -- see "
        "script docstring. Regenerate with "
        "`notebooks/generate_blueprint_draft.py` -- do not hand-edit.",
        "",
    ]

    for depth, title, target in walk_nav(nav):
        if depth == 1:
            continue  # "Unit N" wrapper skipped -- its child carries the heading

        level = min(depth, MAX_HEADING_LEVEL)

        if target is None:
            out.append(f"{'#' * level} {title}")
            out.append("")
            continue

        if Path(target).name.lower() == "index.md":
            continue  # unit overview page -- skipped

        if title:
            out.append(f"{'#' * level} {title}")
            out.append("")

        md_path = DOCS / target
        if not md_path.exists():
            out.append(f"> ⚠️ file not found: `docs/{target}`")
            out.append("")
            continue

        out.extend(extract_page_lines(md_path))
        out.append("")

    OUTPUT.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
