from bs4 import BeautifulSoup

def inspect_file_cols(fpath):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    grid = []
    for r in rows:
        grid.append([])

    for r_idx, row in enumerate(rows):
        cells = row.find_all(['td', 'th'])
        c_idx = 0
        for cell in cells:
            while c_idx < len(grid[r_idx]) and grid[r_idx][c_idx] is not None:
                c_idx += 1
                
            rowspan = int(cell.get('rowspan', 1))
            colspan = int(cell.get('colspan', 1))
            text = cell.get_text(separator=" ", strip=True).replace('\xa0', ' ').strip()
            
            for i in range(rowspan):
                for j in range(colspan):
                    if r_idx + i < len(grid):
                        while len(grid[r_idx + i]) <= c_idx + j:
                            grid[r_idx + i].append(None)
                        grid[r_idx + i][c_idx + j] = text
            c_idx += colspan
            
    print(f"\n--- {fpath} ({len(grid)} rows, {len(grid[0])} cols) ---")
    # print rows that contain category titles to see where they are
    for r_idx, row in enumerate(grid):
        for c_idx, cell in enumerate(row):
            if cell and any(keyword in cell.lower() for keyword in ["girls", "boys", "men", "women"]):
                print(f"Row {r_idx:2d}, Col {c_idx}: '{cell}'")

inspect_file_cols('legacy_pages/46th.html')
inspect_file_cols('legacy_pages/45th.html')
inspect_file_cols('legacy_pages/47th-senior.html')
