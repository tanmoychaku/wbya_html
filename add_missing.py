import re

with open('live_master.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all links
links = re.findall(r'<a.*?href="(.*?)".*?>(.*?)</a>', html, re.IGNORECASE)

missing_cards_html = ""

for href, text in links:
    text = re.sub(r'<.*?>', '', text).strip()
    text = text.replace('\xa0', ' ').replace('\n', ' ')
    
    # We only care about links from 40th downwards
    match = re.search(r'(\d+(?:st|nd|rd|th))\s+National Yoga Championship.*?From\s+(.*?)\s+at\s+(.*)', text, re.IGNORECASE)
    if not match:
        continue
        
    edition = match.group(1)
    
    # Check if edition number is <= 40
    edition_num = int(re.sub(r'\D', '', edition))
    if edition_num > 40:
        continue
        
    date_str = match.group(2).strip()
    location_str = match.group(3).strip()
    
    card_html = f"""
          <a href="{href}" class="result-card">
            <div class="result-edition">{edition} Edition</div>
            <h2 class="result-title">National Yoga Championship</h2>
            <div class="result-meta-list">
              <div class="result-meta-item">
                <svg class="result-meta-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                <span>{date_str}</span>
              </div>
              <div class="result-meta-item">
                <svg class="result-meta-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                <span>{location_str}</span>
              </div>
            </div>
            <div class="result-action">View Full Results</div>
          </a>"""
    missing_cards_html += card_html

# Read the local file
with open('results-national-yoga-championship.html', 'r', encoding='utf-8') as f:
    local_html = f.read()

# Insert the missing cards before the closing div of results-grid
insertion_point = local_html.rfind('        </div>\n      </div>\n    </section>')
if insertion_point != -1:
    new_html = local_html[:insertion_point] + missing_cards_html + '\n' + local_html[insertion_point:]
    with open('results-national-yoga-championship.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully added missing cards.")
else:
    print("Could not find insertion point.")
