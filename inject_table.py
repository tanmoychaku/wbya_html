with open('extracted_article.html', 'r', encoding='utf-8') as f:
    article_html = f.read()

# Remove the article tags to just keep the entry-content
import re
match = re.search(r'<div class="entry-content clearfix">(.*?)</div>\s*</article>', article_html, re.DOTALL)
if match:
    table_content = match.group(1).strip()
else:
    table_content = article_html

with open('results-8th-netaji-subhas-state-games-2022.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<main class="main-content">'
end_marker = '</main>'

start_idx = html.find(start_marker) + len(start_marker)
end_idx = html.find(end_marker)

new_html = html[:start_idx] + '\n    <section class="section">\n      <div class="container">\n' + table_content + '\n      </div>\n    </section>\n  ' + html[end_idx:]

with open('results-8th-netaji-subhas-state-games-2022.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('Updated results-8th-netaji-subhas-state-games-2022.html with original table')
