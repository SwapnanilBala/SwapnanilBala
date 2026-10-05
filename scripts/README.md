# Showcase pipeline

Everything on the profile page is generated from one file, [`data/projects.toml`](../data/projects.toml), plus the screenshots you upload. You never edit the project cards, the academic table or the gallery pages by hand.

```
data/projects.toml            the source of truth: names, summaries, captions, per-image fixes
assets/PREFIX_N.png           the drop zone: raw uploads (consumed by the build)
assets/projects/<slug>/       generated: NN.webp screenshots + hero.webp collage
projects/<slug>.md            generated: one gallery page per project
README.md                     hand-written, except the blocks between <!-- featured:* --> and <!-- academic:* -->
scripts/build.py              the build
.github/workflows/            optional: runs the build for you when you upload from the web
```

## Add screenshots

1. Name each file `PREFIX_N`. The prefix belongs to a project (`LA` Lagna Atelier, `RH` Robust Health, `DA` Appointment Booking, `AN` Alignr, `GW` GridWorld, `BR` BRFSS, `TK` TikTok, `LL` Little Lemon, `RC` Room Cleanliness), and `N` is the order it appears in. Case and separators don't matter: `LA_1.png`, `la-1.PNG` and `La 1.jpeg` are all the same slot.
2. Upload them into `assets/` (GitHub: **Add file → Upload files**).
3. Either wait for the **Build showcase** action (about a minute), or run it yourself:
   ```bash
   pip install pillow          # once, needs Python 3.11+
   python scripts/build.py
   ```
4. To replace a screenshot, upload a new file with the same name. To remove one, delete `assets/projects/<slug>/NN.webp` and run the build.

The build converts each upload to WebP (max 1600px wide, 720px for phone shots), strips metadata, deletes the raw file and rebuilds the hero collage, the project page and the README. Run with `--keep-raw` to keep the originals. GIFs are copied as-is (keep them under about 5 MB).

Raw uploads still live in git history, since you committed them. The build only keeps them out of the working tree.

## Add a project

Copy a `[[project]]` block in `data/projects.toml`, give it a unique `slug` and `prefix`, and set `kind`:

- `product` gets a card with a hero collage in **Featured Work**
- `academic` gets a row in the compact table (and a gallery page as soon as it has screenshots)

Then upload screenshots with its prefix. The comments at the top of the manifest list every key.

## Fix a screenshot without retaking it

In `data/projects.toml`, per project:

```toml
[project.trim_bottom]
1 = 160                       # cut 160px off the bottom of screenshot 1 (e.g. a half-visible footer)

[project.redact]
5 = [[1302, 20, 1534, 52]]    # paint over a box [x0, y0, x1, y1] in screenshot 5 (e.g. an email)
```

Coordinates are pixels of the **original** upload. These are re-applied every time that number is uploaded again, so a fresh screenshot with the same problem gets the same fix.

## How gallery rows are chosen

Screenshots stay in numeric order. Phone-shaped shots (taller than 0.7:1) share a row, up to four. Very wide strips (over 2.2:1) get a row to themselves. Neighbours of similar shape pair up two per row, and anything left over runs full width. So `RH_1` to `RH_4` as phone shots become one row of four, with no layout work.

## Before you upload any screenshot

- No real emails, phone numbers, names or patient data. Use a test account and fake records. (Check navbars: they show the signed-in email.)
- Check the address bar, tabs and pre-filled form fields.
- Retake it if a sticky nav overlaps content or text is clipped, or use `trim_bottom` / `redact` above.
- Show the app doing something (results, charts, confirmation), not only an empty form.
- Read the seed data in the shot. Typos in demo content get noticed.

## If the action can't be added

Pushing a file into `.github/workflows/` needs a token with workflow permission. If that was refused, create `.github/workflows/build-showcase.yml` in the GitHub web editor with the contents from this repo's history, or skip it and run `python scripts/build.py` locally. Nothing else depends on it.
