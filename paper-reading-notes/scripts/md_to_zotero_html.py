import argparse
import html
import re
from pathlib import Path

try:
    import markdown
except ImportError as exc:
    raise SystemExit(
        "Missing dependency: Python-Markdown is required for HTML export. "
        "Install it with: python -m pip install markdown"
    ) from exc


DISPLAY_MATH_RE = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)
INLINE_MATH_RE = re.compile(r"(?<!\\)\$(?!\$)([^$\n]+?)(?<!\\)\$")
LIST_RE = re.compile(r"^(\s*)([-*+] |\d+\. )")


def normalize_markdown_lists(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    raw_lines = text.split("\n")
    adjusted: list[str] = []

    for line in raw_lines:
        if re.match(r"^  ([-*+] |\d+\. )", line):
            line = "  " + line
        adjusted.append(line)

    output: list[str] = []
    prev_nonempty = ""
    for line in adjusted:
        stripped = line.strip()
        is_list = bool(LIST_RE.match(line))
        if (
            is_list
            and output
            and output[-1] != ""
            and prev_nonempty
            and not LIST_RE.match(prev_nonempty)
            and not prev_nonempty.lstrip().startswith("<")
            and not prev_nonempty.startswith("#")
        ):
            output.append("")
        output.append(line)
        if stripped:
            prev_nonempty = line

    return "\n".join(output)


def render_math_for_better_notes(text: str) -> str:
    display_blocks: list[str] = []

    def display_repl(match: re.Match[str]) -> str:
        content = match.group(1).strip("\n")
        block = (
            '\n<pre class="math">$$'
            + html.escape(content, quote=False)
            + "$$</pre>\n"
        )
        display_blocks.append(block)
        return f"\n@@DISPLAY_MATH_BLOCK_{len(display_blocks) - 1}@@\n"

    text = DISPLAY_MATH_RE.sub(display_repl, text)

    def inline_repl(match: re.Match[str]) -> str:
        content = match.group(1)
        return '<span class="math">$' + html.escape(content, quote=False) + "$</span>"

    text = INLINE_MATH_RE.sub(inline_repl, text)

    for idx, block in enumerate(display_blocks):
        text = text.replace(f"@@DISPLAY_MATH_BLOCK_{idx}@@", block)

    return text


def build_html(title: str, body_html: str) -> str:
    css = """
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  color: #1f2937;
  line-height: 1.65;
  margin: 0;
  padding: 0;
  background: #ffffff;
}
.note-shell {
  max-width: 920px;
  margin: 0 auto;
  padding: 28px 36px 48px;
}
h1, h2, h3, h4 {
  color: #111827;
  line-height: 1.25;
}
h1 {
  font-size: 1.9rem;
  border-bottom: 2px solid #e5e7eb;
  padding-bottom: 0.5rem;
  margin-top: 0;
}
h2 {
  font-size: 1.35rem;
  margin-top: 2rem;
  border-left: 4px solid #9ec5fe;
  padding-left: 0.6rem;
}
h3 {
  font-size: 1.1rem;
  margin-top: 1.4rem;
}
p, li {
  font-size: 0.98rem;
}
ul, ol {
  padding-left: 1.4rem;
}
code {
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  background: #f3f4f6;
  border-radius: 4px;
  padding: 0.1rem 0.3rem;
}
pre {
  white-space: pre-wrap;
  word-break: break-word;
}
pre.math,
span.math {
  font-family: "Cambria Math", "STIX Two Math", "Times New Roman", serif;
}
pre.math {
  margin: 1rem 0 1.2rem;
  padding: 0.85rem 1rem;
  background: #f8fafc;
  border-left: 4px solid #cbd5e1;
  border-radius: 6px;
}
blockquote {
  margin: 1rem 0;
  padding: 0.2rem 1rem;
  color: #374151;
  background: #f8fafc;
  border-left: 4px solid #d1d5db;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 1rem 0;
}
th, td {
  border: 1px solid #d1d5db;
  padding: 0.5rem 0.65rem;
  vertical-align: top;
}
th {
  background: #f3f4f6;
  text-align: left;
}
img {
  max-width: 100%;
  height: auto;
}
hr {
  border: none;
  border-top: 1px solid #e5e7eb;
  margin: 2rem 0;
}
"""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>{css}</style>
</head>
<body>
  <div class="note-shell">
{body_html}
  </div>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Markdown paper notes to Better Notes/Zotero-friendly HTML."
    )
    parser.add_argument("input_md", help="Path to Markdown file")
    parser.add_argument("-o", "--output-html", help="Output HTML path", required=True)
    parser.add_argument(
        "--fragment",
        help="Optional output path for body fragment HTML",
        default=None,
    )
    args = parser.parse_args()

    input_path = Path(args.input_md).resolve()
    output_path = Path(args.output_html).resolve()
    fragment_path = Path(args.fragment).resolve() if args.fragment else None

    md_text = input_path.read_text(encoding="utf-8")
    md_text = normalize_markdown_lists(md_text)
    md_text = render_math_for_better_notes(md_text)

    body_html = markdown.markdown(
        md_text,
        extensions=["extra", "sane_lists", "toc"],
        output_format="html5",
    )

    title = input_path.stem
    output_path.write_text(build_html(title, body_html), encoding="utf-8")

    if fragment_path:
        fragment_path.write_text(body_html, encoding="utf-8")

    print(output_path)
    if fragment_path:
        print(fragment_path)


if __name__ == "__main__":
    main()
