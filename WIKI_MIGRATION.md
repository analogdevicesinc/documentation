# Wiki Image Migration Tools

Tools for inventorying, downloading, and referencing images from
`wiki.analog.com` during the migration of wiki pages to this GitHub-hosted
Sphinx repository.

## Dependencies

```bash
pip install requests beautifulsoup4 openpyxl
```

---

## Scripts

### `scrape_wiki_images.py`

Crawls the full wiki sitemap (4,676 pages) and records every image reference.
Produces `wiki_images.xlsx` with two sheets:

| Sheet | Contents |
|---|---|
| **Wiki Images** | Every `(page URL, image name, image URL)` triple — 49,470 rows |
| **Shared Images** | Images used on 2+ pages, with common ancestor path and all referencing pages |

```bash
python3 scrape_wiki_images.py
```

Re-running overwrites `wiki_images.xlsx`. The scrape takes ~10 minutes with 8
concurrent workers.

---

### `add_shared_sheet.py`

Regenerates the **Shared Images** sheet from the existing `wiki_images.xlsx`
without re-scraping the wiki. Useful after any changes to the ancestor/folder
logic.

```bash
python3 add_shared_sheet.py
```

---

### `download_images.py`

Assigns every unique `_media` image to a destination folder, writes a
**Download Plan** sheet to `wiki_images.xlsx`, then downloads all content
images into `docs/`.

```bash
# Write the Download Plan sheet only — no downloading
python3 download_images.py --plan-only

# Write plan + download all images
python3 download_images.py
```

Downloaded images are placed under `docs/` mirroring the wiki namespace:

```
docs/
  resources/
    eval/
      user-guides/images/
      dpg/images/
      developer-kits/images/
      sdp/images/
      …
    fpga/
      altera/images/
      xilinx/images/
      …
    tools-software/
      sigmastudio/images/
      uc-drivers/images/
      sharc-audio-module/images/
      …
  university/
    courses/images/
    tools/images/
    labs/images/
```

85 `images/` folders in total, ~20,400 unique images downloaded.

Images from `/lib/` (site chrome — logos, icons) and external CDNs are
skipped. The **Download Plan** sheet records the skip reason for every
excluded image.

Re-running `download_images.py` is safe — already-downloaded files are
skipped.

---

### `rst_image_lookup.py`

The primary tool for day-to-day migration work. Given a wiki page URL, it
prints ready-to-paste `.. figure::` RST directives with the correct relative
path from the migrated RST file to each image.

#### Look up a specific page

```bash
# Full URL
python3 rst_image_lookup.py https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/hardware

# Partial path (no scheme/host needed)
python3 rst_image_lookup.py resources/eval/user-guides/ad-fmcomms1-ebz/hardware

# Substring — if multiple pages match, they are listed so you can refine
python3 rst_image_lookup.py ad-fmcomms1-ebz/hardware
```

#### Look up multiple pages at once

```bash
python3 rst_image_lookup.py <url1> <url2> <url3>
```

#### List all pages that have content images

```bash
# All pages
python3 rst_image_lookup.py --list-pages

# Filter by substring
python3 rst_image_lookup.py --list-pages inertial-mems/imu
python3 rst_image_lookup.py --list-pages resources/fpga/altera
```

#### Use `.. image::` instead of `.. figure::`

```bash
python3 rst_image_lookup.py --no-figure <url>
```

#### Example output

```
========================================================================
Wiki page : https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/hardware
RST file  : docs/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/index.rst
========================================================================

Content images (3):

.. figure:: ../../images/pin_diagram.png
   :align: center

   pin_diagram.png
   {'# image source': 'https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/pin_diagram.png'}

...

Skipped (4 — site chrome / external CDN):
  [site chrome (/lib/)]  diff.png  ...
```

The `# image source` comment is a migration aid — remove it from the final
RST file.

---

## How image paths are assigned

Images are stored according to their **`_media` namespace** on the wiki, not
the page that uses them. This is the authoritative location in DokuWiki.

| `_media` path prefix | Destination folder |
|---|---|
| `/_media/resources/eval/<sub>/…` | `resources/eval/<sub>/images/` |
| `/_media/resources/fpga/<sub>/…` | `resources/fpga/<sub>/images/` |
| `/_media/resources/tools-software/<sub>/…` | `resources/tools-software/<sub>/images/` |
| `/_media/university/<sub>/…` | `university/<sub>/images/` |
| `/_media/resources/<other>/…` | `resources/<other>/images/` |
| `/lib/…` or external host | **skipped** |

The alias `user-guide` → `user-guides` is normalised automatically so both
wiki namespace variants land in the same folder.

---

## RST path logic

The `rst_image_lookup.py` tool computes relative paths using `os.path.relpath`
from the RST file directory to the image file. Two cases arise:

**Same namespace** — image lives in the ancestor folder of the page:
```rst
.. figure:: ../../images/board_photo.jpg
```

**Cross-namespace** — page borrows an image owned by a different namespace:
```rst
.. figure:: ../../fpga/altera/images/eclipseprojects.png
```

About 37% of wiki pages reference at least one image from a different
namespace. The tool handles both cases automatically.

---

## Migration workflow

1. **Find pages to migrate**
   ```bash
   python3 rst_image_lookup.py --list-pages resources/eval/user-guides
   ```

2. **Get image directives for a page**
   ```bash
   python3 rst_image_lookup.py https://wiki.analog.com/resources/eval/user-guides/<page>
   ```

3. **Convert wiki markup to RST** using the
   [DokuWiki to Sphinx script](https://gist.github.com/gastmaier/9d9c8281dc3c8551991a857cdb2692cc),
   then paste in the `.. figure::` blocks from step 2.

4. **Remove the `# image source` comments** from the final RST file.

5. **Build and verify**
   ```bash
   cd docs && make html
   ```

---

## Output files

| File | Description |
|---|---|
| `wiki_images.xlsx` | Master spreadsheet — Wiki Images, Shared Images, Download Plan sheets |
| `docs/*/images/` | Downloaded images, ~20,400 files across 85 folders |
