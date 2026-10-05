#!/usr/bin/env python3
"""Image helper for the profile README.

    python scripts/assets.py optimize [--force]   # assets/_inbox/<project>/*  ->  assets/projects/<project>/*.webp
    python scripts/assets.py gallery              # rebuild the gallery block in projects/<project>.md

Needs Pillow:  pip install pillow
"""
import argparse
import html
import re
import shutil
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "assets" / "_inbox"
OUT = ROOT / "assets" / "projects"
PAGES = ROOT / "projects"

MAX_WIDTH = 1600
QUALITY = 82
COVER_RATIO = (16, 10)
RASTER = {".png", ".jpg", ".jpeg", ".webp"}
GIF_WARN_MB = 5
BIG_WARN_KB = 300
START, END = "<!-- gallery:start -->", "<!-- gallery:end -->"


def slugify(stem):
    return re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-") or "image"


def center_crop(im, ratio):
    rw, rh = ratio
    w, h = im.size
    if w / h > rw / rh:
        nw = round(h * rw / rh)
        x = (w - nw) // 2
        return im.crop((x, 0, x + nw, h))
    nh = round(w * rh / rw)
    y = (h - nh) // 2
    return im.crop((0, y, w, y + nh))


def load_rgb(path):
    im = ImageOps.exif_transpose(Image.open(path))
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        flat = Image.new("RGB", im.size, "white")
        flat.paste(im, mask=im.getchannel("A"))
        return flat
    return im.convert("RGB")


def optimize(force):
    if not INBOX.is_dir():
        INBOX.mkdir(parents=True)
        print(f"Created {INBOX.relative_to(ROOT)}/. Put images in <project>/ subfolders there and run again.")
        return

    converted = skipped = 0
    before = after = 0
    for project in sorted(p for p in INBOX.iterdir() if p.is_dir()):
        dest_dir = OUT / project.name
        for src in sorted(project.iterdir()):
            ext = src.suffix.lower()
            if ext != ".gif" and ext not in RASTER:
                continue
            name = slugify(src.stem)
            dest_dir.mkdir(parents=True, exist_ok=True)

            if ext == ".gif":
                dest = dest_dir / f"{name}.gif"
                if dest.exists() and not force:
                    skipped += 1
                    continue
                shutil.copyfile(src, dest)
                mb = dest.stat().st_size / 1024 / 1024
                note = f"  <-- over {GIF_WARN_MB} MB, consider trimming or shrinking it" if mb > GIF_WARN_MB else ""
                print(f"{dest.relative_to(ROOT)}  {mb:.1f} MB (copied as-is){note}")
                converted += 1
                continue

            dest = dest_dir / f"{name}.webp"
            if dest.exists() and not force:
                skipped += 1
                continue
            im = load_rgb(src)
            if name == "cover":
                im = center_crop(im, COVER_RATIO)
            if im.width > MAX_WIDTH:
                im = im.resize((MAX_WIDTH, round(im.height * MAX_WIDTH / im.width)), Image.LANCZOS)
            # No exif= passed, so camera/GPS metadata is dropped.
            im.save(dest, "WEBP", quality=QUALITY, method=6)
            kb = dest.stat().st_size // 1024
            note = f"  <-- over {BIG_WARN_KB} KB" if kb > BIG_WARN_KB else ""
            print(f"{dest.relative_to(ROOT)}  {kb} KB{note}")
            before += src.stat().st_size
            after += dest.stat().st_size
            converted += 1

    print(f"\n{converted} converted, {skipped} skipped (already exist; use --force to redo).")
    if before:
        print(f"Raster images: {before / 1024 / 1024:.1f} MB -> {after / 1024 / 1024:.1f} MB.")
    print("Originals stay in assets/_inbox/ (gitignored). Run `gallery` next.")


def caption(path):
    text = re.sub(r"^\d+[-_ ]*", "", path.stem).replace("-", " ").replace("_", " ").strip()
    return (text[:1].upper() + text[1:]) if text else path.stem


def gallery_block(slug):
    folder = OUT / slug
    images = sorted(
        p for p in folder.iterdir()
        if p.is_file() and p.stem != "cover" and p.suffix.lower() in RASTER | {".gif"}
    )
    if not images:
        return ""
    cells = []
    for p in images:
        cap = html.escape(caption(p))
        cells.append(
            f'<td width="50%" valign="top">'
            f'<img src="../assets/projects/{slug}/{p.name}" alt="{cap}" width="100%"><br><sub>{cap}</sub>'
            f"</td>"
        )
    if len(cells) % 2:
        cells.append('<td width="50%"></td>')
    rows = [f"<tr>\n{cells[i]}\n{cells[i + 1]}\n</tr>" for i in range(0, len(cells), 2)]
    return "## Screenshots\n\n<table>\n" + "\n".join(rows) + "\n</table>"


def gallery():
    pages = sorted(p for p in PAGES.glob("*.md") if not p.name.startswith("_"))
    if not pages:
        print("No project pages found in projects/.")
        return
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    for page in pages:
        slug = page.stem
        text = page.read_text(encoding="utf-8")
        if not pattern.search(text):
            print(f"{page.name}: no {START} / {END} markers, skipped")
            continue
        if not (OUT / slug).is_dir():
            print(f"{page.name}: no assets/projects/{slug}/ folder, skipped")
            continue
        block = gallery_block(slug)
        new = pattern.sub(lambda _: f"{START}\n{block}\n{END}" if block else f"{START}\n{END}", text)
        if new != text:
            page.write_text(new, encoding="utf-8")
        count = block.count("<img ")
        print(f"{page.name}: {count} screenshot{'s' if count != 1 else ''}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    opt = sub.add_parser("optimize", help="convert inbox images to 1600px WebP")
    opt.add_argument("--force", action="store_true", help="overwrite images that already exist")
    sub.add_parser("gallery", help="rebuild gallery blocks in projects/*.md")
    args = parser.parse_args()
    optimize(args.force) if args.cmd == "optimize" else gallery()


if __name__ == "__main__":
    sys.exit(main())
