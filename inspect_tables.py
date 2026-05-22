import os
import glob
from bs4 import BeautifulSoup

files = sorted(glob.glob('legacy_pages/*.html'))
print(f"Found {len(files)} files")

for fpath in files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    entry = soup.find('div', class_='entry-content')
    if not entry:
        print(f"{os.path.basename(fpath)}: No entry-content")
        continue
    table = entry.find('table')
    if not table:
        print(f"{os.path.basename(fpath)}: No table")
        continue
    
    # Let's inspect the first few rows and count columns
    rows = table.find_all('tr')
    max_cols = 0
    for r in rows:
        cells = r.find_all(['td', 'th'])
        col_count = sum(int(c.get('colspan', 1)) for c in cells)
        if col_count > max_cols:
            max_cols = col_count
            
    print(f"{os.path.basename(fpath)}: max cols = {max_cols}, rows = {len(rows)}")
