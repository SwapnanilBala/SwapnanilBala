# Adding images

Raw screenshots never get committed. They go through an inbox, get shrunk to 1600px WebP, and the gallery pages are generated from whatever ends up in each project's folder.

```
assets/_inbox/<project>/     raw originals (gitignored, stays on your machine)
assets/projects/<project>/   optimized WebP/GIF (committed, what the README uses)
projects/<project>.md        one page per project, gallery generated into it
```

## Workflow

```bash
pip install pillow                       # once
cp ~/Desktop/*.png assets/_inbox/astro-app/
python scripts/assets.py optimize        # inbox -> assets/projects/astro-app/*.webp
python scripts/assets.py gallery         # rebuild gallery blocks in projects/*.md
git add -A && git commit -m "Add Astro App screenshots" && git push
```

No Python handy? Use [squoosh.app](https://squoosh.app): resize to 1600px wide, WebP at quality ~80, save into `assets/projects/<project>/`, then run `gallery` (or write the page by hand).

## Naming rules

- Files in the inbox become `kebab-case.webp`. Name them `NN-what-it-shows`: `02-generated-chart.png` becomes `02-generated-chart.webp`, sorts second, and gets the caption "Generated chart".
- A file named `cover` is center-cropped to 16:10 so the cards in the README line up. Crop it yourself first if the middle isn't the interesting part.
- GIFs are copied as-is. Keep them under ~5 MB (the script warns).
- EXIF/GPS metadata is stripped on conversion.
- `optimize` skips files that already exist. `--force` redoes them.

## Adding a new project

1. `mkdir assets/_inbox/<slug>` and drop images in, including a `cover.png`.
2. `python scripts/assets.py optimize`
3. `cp projects/_template.md projects/<slug>.md`, then replace `PROJECT-SLUG`, the title, description and links.
4. `python scripts/assets.py gallery`
5. Add a card or row in the root `README.md`.

Folders already created and waiting for images: `gridworld`, `brfss-dashboard`, `tiktok-copyright-analyzer`, `little-lemon-database`, `room-cleanliness-detector`.

## Before you upload any screenshot

- No real emails, phone numbers, names or patient data. Use a test account and fake records.
- Check the address bar, tabs and any pre-filled form fields.
- Retake the shot if a sticky nav overlaps content or text is clipped.
- Show the app *doing something* (results, charts, confirmation), not an empty form.
