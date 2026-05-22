from bs4 import BeautifulSoup

fpath = 'legacy_pages/41st.html'
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

print(f"Grid dimensions: {len(grid)} rows x {len(grid[0])} cols")
for r_idx, row in enumerate(grid[:15]):
    print(f"Row {r_idx:2d}: {row}")
