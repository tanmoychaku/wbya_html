import re
from bs4 import BeautifulSoup

def is_rank(text):
    text = text.lower().strip()
    # matches '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th' etc.
    if re.search(r'^\d+(st|nd|rd|th)?$', text):
        return True
    return False

def clean_name(text):
    # remove trailing/leading spaces and standard cleanups
    return text.strip()

def parse_slice(grid, col_indices):
    categories = []
    active_cat = None
    
    # Skip top banner rows (rows containing date, venue, main championship title)
    # We can detect this if a row has a single merged cell containing 'held at', 'date:', 'championship', etc.
    start_parsing = False
    
    for r_idx, row in enumerate(grid):
        # Extract cell values for the column indices in this slice
        slice_cells = [row[c] if c < len(row) else '' for c in col_indices]
        
        # Filter out None and empty cells
        non_empty = [c for c in slice_cells if c]
        if not non_empty:
            continue
            
        unique = list(dict.fromkeys(non_empty))
        text_line = " ".join(unique)
        
        # Detect main championship headers to ignore
        if not start_parsing:
            # We start parsing when we see a category keyword in a single merged cell or multiple cells
            # but NOT main title banners. E.g., "8 to 11 Girls" or "Group A"
            if any(keyword in text_line.lower() for keyword in ["girls", "boys", "men", "women", "group", "single", "pair", "solo", "rhythmic", "artistic"]):
                if not any(k in text_line.lower() for k in ["held at", "date:", "venue:", "championship", "winner :", "runners up"]):
                    start_parsing = True
            
            if not start_parsing:
                continue
                
        # Is it a category header?
        # A category header typically has 1 unique text spanning the columns
        is_header = False
        if len(unique) == 1:
            val = unique[0]
            # Must not be a rank
            if not is_rank(val) and not val.isdigit():
                # Must contain category keywords
                if any(keyword in val.lower() for keyword in ["girls", "boys", "men", "women", "group", "single", "pair", "solo", "rhythmic", "artistic", "yogasana"]):
                    is_header = True
                    
        if is_header:
            if active_cat:
                categories.append(active_cat)
            active_cat = {"title": unique[0], "winners": []}
            # print(f"Category: {unique[0]}")
        else:
            # It's a winner candidate row if we have an active category
            if active_cat:
                # We expect at least one rank and one name
                rank_val = None
                name_val = None
                extra_val = None
                
                # Identify which cell is rank and which is name
                for val in non_empty:
                    val_str = val.strip()
                    if is_rank(val_str):
                        rank_val = val_str
                    elif len(val_str) > 1 and not val_str.isdigit():
                        if not name_val:
                            name_val = val_str
                        else:
                            extra_val = val_str
                            
                if rank_val and name_val:
                    # check for duplicate name in active category
                    exists = any(w['name'] == name_val for w in active_cat["winners"])
                    if not exists:
                        active_cat["winners"].append({
                            "rank": rank_val,
                            "name": name_val,
                            "extra": extra_val
                        })
                        # print(f"  {rank_val}: {name_val} (extra: {extra_val})")
                        
    if active_cat:
        categories.append(active_cat)
        
    return categories

def process_file_smart(fpath):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    table = soup.find('table')
    if not table:
        return []
        
    rows = table.find_all('tr')
    grid = [[] for _ in rows]

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

    N = len(grid[0])
    if N <= 10:
        S = 4
    else:
        S = 5
        
    left_indices = list(range(1, S))
    right_indices = list(range(S + 1, N - 1))
    
    print(f"File: {fpath}, Columns: {N}, Split: {S}")
    print("=== LEFT SLICE ===")
    left_cats = parse_slice(grid, left_indices)
    for c in left_cats:
        print(f"Cat: {c['title']}")
        for w in c['winners']:
            print(f"  {w['rank']} -> {w['name']} ({w['extra']})")
            
    print("=== RIGHT SLICE ===")
    right_cats = parse_slice(grid, right_indices)
    for c in right_cats:
        print(f"Cat: {c['title']}")
        for w in c['winners']:
            print(f"  {w['rank']} -> {w['name']} ({w['extra']})")

process_file_smart('legacy_pages/41st.html')
