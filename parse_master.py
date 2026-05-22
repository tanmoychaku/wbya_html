import re

with open('live_master.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Try to find the list of links
links = re.findall(r'<a.*?href="(.*?)".*?>(.*?)</a>', html, re.IGNORECASE)
for href, text in links:
    text = re.sub(r'<.*?>', '', text).strip()
    if 'national' in href.lower() and text:
        print(f"Text: {text} | Link: {href}")
