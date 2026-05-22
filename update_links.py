import re

with open('results-national-yoga-championship.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all links
links = re.findall(r'<a href="(http://www.westbengalyogaassociation.org/.*?)"', html)

for link in links:
    match = re.search(r'/(\d+(?:st|nd|rd|th))-', link)
    if match:
        edition = match.group(1)
        new_link = f"results-{edition}-national-yogasana-sports-championship.html"
        html = html.replace(link, new_link)

with open('results-national-yoga-championship.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated all links in the master page.")
