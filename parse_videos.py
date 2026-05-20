import re
import os

html_path = '/Users/chaku/.gemini/antigravity-ide/brain/8e601259-ebff-4215-949e-44a7ea95f821/.system_generated/steps/277/content.md'

with open(html_path, 'r') as f:
    content = f.read()

# Just extract all links containing youtu and the number that precedes them
rows = re.findall(r'<tr.*?>(.*?)</tr>', content, re.DOTALL | re.IGNORECASE)
videos = []

for row in rows:
    tds = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL | re.IGNORECASE)
    # The structure could be [no1, link1, no2, link2] or [no1, link1, divider, no2, link2]
    # Let's extract any pair of consecutive tds where td1 has a number and td2 has a link
    for i in range(len(tds) - 1):
        td_text = re.sub(r'<[^>]+>', '', tds[i]).strip()
        if td_text.isdigit():
            a_match = re.search(r'<a.*?href="([^"]+)".*?>(.*?)</a>', tds[i+1], re.DOTALL | re.IGNORECASE)
            if a_match:
                videos.append({"no": int(td_text), "name": re.sub(r'<[^>]+>', '', a_match.group(2)).strip(), "url": a_match.group(1).strip()})

videos.sort(key=lambda x: x['no'])

html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <base href="../" />
  <title>Syllabus and Guidelines (Videos) | West Bengal Yoga Association</title>
  <link rel="stylesheet" href="assets/css/styles.css" />
  <link rel="stylesheet" href="assets/css/members.css" />
  <style>
    .videos-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 16px;
      margin-top: 32px;
    }
    .video-card {
      background: rgba(255, 255, 255, 0.8);
      border: 1px solid rgba(22, 101, 52, 0.1);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      align-items: center;
      gap: 16px;
      transition: all 0.2s ease;
      text-decoration: none;
      color: var(--color-text);
    }
    .video-card:hover {
      background: white;
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
      border-color: rgba(22, 101, 52, 0.3);
    }
    .video-no {
      background: var(--color-primary);
      color: white;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 600;
      font-size: 0.9rem;
      flex-shrink: 0;
    }
    .video-name {
      font-weight: 500;
      line-height: 1.4;
      text-transform: capitalize;
    }
    .video-icon {
      margin-left: auto;
      color: var(--color-primary);
      opacity: 0.5;
    }
    .video-card:hover .video-icon {
      opacity: 1;
    }
  </style>
</head>
<body>
  <div data-layout-slot="header"></div>

  <main class="main-content">
    <section class="section">
      <div class="container">
        <header class="section-header">
          <p class="section-eyebrow">Championship</p>
          <h1 class="section-title">Syllabus &amp; Guidelines Videos</h1>
          <p class="section-description">Watch the instructional videos for the State Yoga Championship syllabus.</p>
        </header>

        <div class="videos-grid">
"""

for v in videos:
    name_clean = v['name'].replace('&nbsp;', '').strip().title()
    html += f"""          <a href="{v['url']}" target="_blank" rel="noopener" class="video-card">
            <span class="video-no">{v['no']}</span>
            <span class="video-name">{name_clean}</span>
            <svg class="video-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polygon points="5 3 19 12 5 21 5 3"></polygon>
            </svg>
          </a>\n"""

html += """        </div>
      </div>
    </section>
  </main>

  <div data-layout-slot="footer"></div>
  <script src="assets/js/main.js"></script>
</body>
</html>
"""

os.makedirs('championship', exist_ok=True)
with open('championship/syllabus-videos.html', 'w') as f:
    f.write(html)
print(f"Generated championship/syllabus-videos.html with {len(videos)} videos")
