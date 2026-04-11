import argparse
import json
from pathlib import Path

import fitz


def parse_pages(spec: str | None) -> set[int] | None:
    if not spec:
        return None
    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start = int(start_s)
            end = int(end_s)
            for p in range(start, end + 1):
                pages.add(p)
        else:
            pages.add(int(part))
    return pages


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract embedded images directly from a PDF."
    )
    parser.add_argument("pdf", help="Path to the PDF file")
    parser.add_argument(
        "-o",
        "--outdir",
        help="Output directory",
        default=None,
    )
    parser.add_argument(
        "--pages",
        help="1-based page list, e.g. 1,3,5-7",
        default=None,
    )
    parser.add_argument(
        "--min-width",
        type=int,
        default=0,
        help="Skip images narrower than this",
    )
    parser.add_argument(
        "--min-height",
        type=int,
        default=0,
        help="Skip images shorter than this",
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf).expanduser().resolve()
    outdir = (
        Path(args.outdir).expanduser().resolve()
        if args.outdir
        else pdf_path.with_suffix("")
    )
    outdir.mkdir(parents=True, exist_ok=True)

    wanted_pages = parse_pages(args.pages)
    doc = fitz.open(pdf_path)
    manifest: list[dict] = []

    for page_index in range(len(doc)):
        page_no = page_index + 1
        if wanted_pages is not None and page_no not in wanted_pages:
            continue

        page = doc[page_index]
        for image_index, image_info in enumerate(page.get_images(full=True), start=1):
            xref = image_info[0]
            base = doc.extract_image(xref)
            width = int(base["width"])
            height = int(base["height"])
            if width < args.min_width or height < args.min_height:
                continue

            ext = base["ext"]
            out_name = f"page_{page_no:03d}_img_{image_index:02d}_xref_{xref}.{ext}"
            out_path = outdir / out_name
            out_path.write_bytes(base["image"])

            manifest.append(
                {
                    "page": page_no,
                    "image_index": image_index,
                    "xref": xref,
                    "width": width,
                    "height": height,
                    "ext": ext,
                    "path": str(out_path),
                }
            )

    manifest_path = outdir / "manifest.json"
    manifest_path.write_text(
        json.dumps(
            {
                "pdf": str(pdf_path),
                "count": len(manifest),
                "images": manifest,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Extracted {len(manifest)} images to {outdir}")
    print(manifest_path)


if __name__ == "__main__":
    main()
