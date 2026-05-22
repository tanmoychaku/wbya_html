import os
import re
import glob
from bs4 import BeautifulSoup

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | West Bengal Yoga Association</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Signika:wght@400;600;700&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="assets/css/styles.css" />
  <style>
    .results-header { text-align: center; margin-bottom: 24px; }
    .results-header h2 { font-size: 1.5rem; color: #e11d48; font-weight: 800; margin-bottom: 8px; }
    .results-header p { color: #475569; font-size: 1.1rem; font-weight: 600; }
    .standings-banner {
      background: #192135;
      border-radius: 16px; padding: 24px; margin-bottom: 32px; color: white;
      display: flex; flex-wrap: wrap; justify-content: space-around; gap: 16px;
      box-shadow: 0 10px 25px rgba(15, 23, 42, 0.15);
    }
    .standing-item { display: flex; flex-direction: column; align-items: center; text-align: center; }
    .standing-label { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em; color: #94a3b8; margin-bottom: 4px; font-family: 'Inter', sans-serif; }
    .standing-value { font-size: 1.25rem; font-weight: 800; color: #f8fafc; font-family: 'Signika', sans-serif; }
    .standing-value.winner { color: #fef08a; font-size: 1.5rem; }
    .category-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 24px; margin-top: 32px; }
    .category-card { background: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05); display: flex; flex-direction: column; transition: transform 0.2s ease, box-shadow 0.2s ease; }
    .category-card:hover { transform: translateY(-4px); box-shadow: 0 12px 25px rgba(0, 0, 0, 0.1); }
    .category-title { background: #111827; color: #ffffff; padding: 16px 20px; font-size: 1.05rem; font-weight: 700; text-align: center; margin: 0; line-height: 1.4; border-bottom: 3px solid #e11d48; font-family: 'Inter', sans-serif; text-transform: uppercase; }
    .winners-list { padding: 16px; display: flex; flex-direction: column; gap: 12px; }
    .winner-item { display: flex; align-items: center; gap: 16px; padding: 12px; background: #ffffff; border-radius: 8px; border: 1px solid rgba(0,0,0,0.06); box-shadow: 0 2px 5px rgba(0,0,0,0.02); }
    .winner-rank { width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-weight: 800; font-size: 0.95rem; flex-shrink: 0; font-family: 'Inter', sans-serif; }
    .rank-1 { background: #fef08a; color: #854d0e; box-shadow: 0 0 15px rgba(234, 179, 8, 0.3); }
    .rank-2 { background: #e2e8f0; color: #334155; }
    .rank-3 { background: #ffedd5; color: #9a3412; }
    .winner-info { flex: 1; }
    .winner-name { font-family: 'Signika', sans-serif; font-weight: 700; color: #1e293b; font-size: 1.15rem; margin-bottom: 2px; text-transform: capitalize; }
    .winner-desc { font-size: 0.85rem; color: #64748b; }
  </style>
</head>
<body>
  <div data-layout-slot="background"></div>
  <div data-layout-slot="header"></div>

  <main class="main-content">
    <section class="page-hero members-page-hero">
      <div class="container hero-card">
        <span class="section-label">Results</span>
        <h1 class="page-title">{title}</h1>
        <p class="page-copy">{subtitle}</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        
        {standings_html}

        <div class="category-grid">
          {cards_html}
        </div>

      </div>
    </section>
  </main>

  <div data-layout-slot="footer"></div>
  <script src="assets/js/main.js"></script>
</body>
</html>
"""

def extract_meta(soup):
    title_elem = soup.find('h1', class_='entry-title')
    title = title_elem.text.strip() if title_elem else "National Yoga Championship"

    og_desc = soup.find('meta', property='og:description')
    desc = og_desc['content'] if og_desc else ""
    
    subtitle = ""
    winner = ""
    runner_up = ""
    
    if "Date:" in desc or "Held at :" in desc:
        subtitle = re.sub(r'Winner.*', '', desc, flags=re.IGNORECASE).strip()
        winner_match = re.search(r'Winner\s*:\s*([^R\n]+)', desc, re.IGNORECASE)
        if winner_match:
            winner = winner_match.group(1).strip()
            
        runner_up_match = re.search(r'Runners Up\s*:\s*([^\n]+)', desc, re.IGNORECASE)
        if runner_up_match:
            runner_up = runner_up_match.group(1).strip()

    standings_html = ""
    if winner or runner_up:
        standings_html = '<div class="standings-banner">'
        if winner:
            standings_html += f'''
          <div class="standing-item">
            <span class="standing-label">Overall Winner</span>
            <span class="standing-value winner">{winner}</span>
          </div>'''
        if runner_up:
            standings_html += f'''
          <div class="standing-item">
            <span class="standing-label">1st Runners Up</span>
            <span class="standing-value">{runner_up}</span>
          </div>'''
        standings_html += '</div>'
        
    return title, subtitle, standings_html

def get_rank_class(rank_str):
    r = rank_str.lower()
    if '1' in r or 'first' in r: return 'rank-1'
    if '2' in r or 'second' in r: return 'rank-2'
    if '3' in r or 'third' in r: return 'rank-3'
    return ''

def is_category_header(text):
    if not text: return False
    text = text.lower()
    if re.search(r'(boys|girls|men|women|group|above|years|single|pair|rhythmic|artistic|yogasana)', text):
        if len(text) < 60:
            return True
    return False

def parse_table_to_cards(html):
    soup = BeautifulSoup(html, 'html.parser')
    entry = soup.find('div', class_='entry-content')
    if not entry:
        return ""

    table = entry.find('table')
    if not table:
        return ""

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
            text = cell.get_text(separator=" ", strip=True).replace('\\xa0', ' ').strip()
            
            for i in range(rowspan):
                for j in range(colspan):
                    if r_idx + i < len(grid):
                        while len(grid[r_idx + i]) <= c_idx + j:
                            grid[r_idx + i].append(None)
                        grid[r_idx + i][c_idx + j] = text
            c_idx += colspan

    categories = []
    active_cats = {} # col_index -> {"title": "", "winners": []}

    for row in grid:
        for c_idx, cell in enumerate(row):
            if not cell: continue
            
            # Is it a header?
            if is_category_header(cell) and not re.match(r'^(1st|2nd|3rd|\d)$', cell.lower()):
                # Start a new category for this column
                if c_idx in active_cats and active_cats[c_idx]["winners"]:
                    categories.append(active_cats[c_idx])
                
                active_cats[c_idx] = {"title": cell, "winners": []}
                
                # If colspan > 1, the adjacent cells might be None, but they belong to this column.
                # We'll just map them to the starting c_idx.
            
            # Is it a rank/winner row?
            elif re.match(r'^(\d+(st|nd|rd|th)?|\d)$', cell.lower()):
                # This cell looks like a rank. 
                # Let's find which category it belongs to by looking at its c_idx or nearest left c_idx.
                target_cat_col = None
                for col in reversed(range(c_idx + 1)):
                    if col in active_cats:
                        target_cat_col = col
                        break
                
                if target_cat_col is not None:
                    # Look ahead for name
                    rank = cell
                    name = ""
                    pos = ""
                    # The name is usually the next non-empty cell in the row
                    n_idx = c_idx + 1
                    while n_idx < len(row) and not row[n_idx]:
                        n_idx += 1
                    if n_idx < len(row):
                        name = row[n_idx]
                        
                        # Sometimes there's a 3rd cell (e.g. 1st, 2nd, 3rd)
                        p_idx = n_idx + 1
                        while p_idx < len(row) and not row[p_idx]:
                            p_idx += 1
                        if p_idx < len(row):
                            pos = row[p_idx]
                            
                            # If `pos` is actually the rank (like '1st'), swap them
                            if re.match(r'^(\d+(st|nd|rd|th)?)$', pos.lower()) and re.match(r'^\d$', rank):
                                rank = pos
                                pos = ""
                    
                    # Avoid duplicates since we might hit the same merged cell again
                    if name:
                        # Check if we already added this winner to this category (due to rowspan)
                        exists = any(w['name'] == name for w in active_cats[target_cat_col]["winners"])
                        if not exists:
                            active_cats[target_cat_col]["winners"].append({
                                "rank": rank,
                                "name": name,
                                "pos": pos
                            })

    # Flush remaining
    for c_idx, cat in active_cats.items():
        if cat["winners"] or cat["title"]:
            categories.append(cat)

    # Generate HTML
    cards_html = ""
    for cat in categories:
        if not cat["winners"]: continue
        
        cards_html += f'''
          <div class="category-card">
            <h3 class="category-title">{cat["title"]}</h3>
            <div class="winners-list">
'''
        for w in cat["winners"]:
            rank_class = get_rank_class(w['rank'])
            rank_disp = w['rank']
            if rank_disp.isdigit():
                rank_disp += "th"
                if rank_disp.startswith('1'): rank_disp = "1st"
                if rank_disp.startswith('2'): rank_disp = "2nd"
                if rank_disp.startswith('3'): rank_disp = "3rd"
                
            cards_html += f'''
              <div class="winner-item">
                <div class="winner-rank {rank_class}">{rank_disp}</div>
                <div class="winner-info">
                  <div class="winner-name">{w['name']}</div>
                  {"<div class='winner-desc'>" + w['pos'] + "</div>" if w['pos'] and w['pos'] != rank_disp else ""}
                </div>
              </div>
'''
        cards_html += '''
            </div>
          </div>
'''

    # If heuristic failed to find anything, return raw table with exact 47th styling
    if not cards_html.strip():
        cards_html = f'<div class="legacy-table-wrapper">{entry.decode_contents()}</div>'

    return cards_html

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    title, subtitle, standings = extract_meta(soup)
    cards_html = parse_table_to_cards(html)

    final_html = TEMPLATE.replace('{title}', title).replace('{subtitle}', subtitle).replace('{standings_html}', standings).replace('{cards_html}', cards_html)

    filename = os.path.basename(filepath)
    edition = filename.replace('.html', '')
    new_filepath = f"results-{edition}-national-yogasana-sports-championship.html"
    if 'junior' in filepath or '46th' in filepath:
        new_filepath = filepath.replace('legacy_pages\\', '')
    
    with open(new_filepath, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"Generated {new_filepath}")

if __name__ == "__main__":
    files = glob.glob('legacy_pages/*.html')
    print(f"Processing {len(files)} legacy pages with advanced parser...")
    for f in files:
        process_file(f)
