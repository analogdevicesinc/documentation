# Wiki Downloads Scraper

Crawls all pages listed in the `wiki.analog.com` sitemap and collects every
downloadable file linked from each page (PDFs, ZIP archives, binaries,
spreadsheets, scripts, etc.).

## Output

`wiki_downloads.xlsx` — two sheets:

| Sheet | Contents |
|---|---|
| **All Downloads** | One row per `(wiki page, file)` — page URL, link text, file name, file URL, host, extension |
| **Summary** | One row per unique file URL, sorted by how many pages reference it. Rows highlighted green where the same file appears on 2+ pages. All referencing page URLs spread across columns. |

### File counts from last run (Feb 2026)

| Metric | Value |
|---|---|
| Pages crawled | 4,676 |
| Total download references | 4,996 |
| Unique files | 3,374 |

Top extensions found: `.zip` (2,336) · `.pdf` (1,924) · `.exe` (127) ·
`.xls/.xlsx` (207) · `.tar.gz` (65) · `.py` (52) · `.bin` / `.hex` (85)

Top hosts: `wiki.analog.com` · `swdownloads.analog.com` · `www.analog.com` ·
`github.com` · `events.static.linuxfound.org` · `www.xilinx.com`

---

## Dependencies

```bash
pip install requests beautifulsoup4 openpyxl
```

---

## Usage

Run from the `tmp_migration_utilities/` directory (or any location — the
output file path is absolute):

```bash
python3 scrape_wiki_downloads.py
```

The script will:
1. Fetch and decompress the wiki sitemap (~4,600 pages)
2. Scrape all pages concurrently (8 workers)
3. Print progress every 100 pages and a breakdown by extension/host at the end
4. Write `wiki_downloads.xlsx` into this folder

Typical runtime: **8–12 minutes**.

Re-running overwrites `wiki_downloads.xlsx` with fresh data.

---

## File types detected

The script looks for links ending in any of the following extensions:

| Category | Extensions |
|---|---|
| Documents | `.pdf` `.docx` `.doc` `.pptx` `.ppt` `.xlsx` `.xls` `.csv` |
| Archives | `.zip` `.tar.gz` `.tar.bz2` `.tar.xz` `.tgz` `.gz` `.bz2` `.xz` `.lzma` `.rar` `.7z` |
| Executables / installers | `.exe` `.msi` `.dmg` `.deb` `.rpm` |
| Firmware / binaries | `.bin` `.hex` `.elf` `.img` `.iso` |
| Scripts | `.py` `.sh` `.bat` |
| Data / config | `.json` `.xml` `.mat` `.m` `.ldf` `.uci` |

---

## Output columns — All Downloads sheet

| Column | Description |
|---|---|
| Wiki Page URL | The wiki page where the link was found |
| Link Text | The visible anchor text of the download link |
| File Name | Filename extracted from the URL path |
| File URL | Full absolute URL of the downloadable file |
| Host | Domain serving the file |
| Extension | Detected file extension |

## Output columns — Summary sheet

| Column | Description |
|---|---|
| File URL | Clean URL (no query string) of the unique file |
| File Name | Filename |
| Host | Domain serving the file |
| Extension | File extension |
| Page Count | Number of wiki pages that link to this file |
| Wiki Page 1 … N | Each referencing wiki page URL |
