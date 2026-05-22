import sys
import re

filename = sys.argv[1] if len(sys.argv) > 1 else '47th-senior.html'
with open(filename, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract table rows
trs = re.findall(r'<tr.*?>(.*?)</tr>', html, re.IGNORECASE | re.DOTALL)
for tr in trs:
    tds = re.findall(r'<t[dh].*?>(.*?)</t[dh]>', tr, re.IGNORECASE | re.DOTALL)
    cleaned_tds = []
    for td in tds:
        clean = re.sub(r'<.*?>', '', td)
        clean = clean.replace('&nbsp;', ' ').replace('&#8211;', '-').strip()
        if clean:
            cleaned_tds.append(clean)
    if cleaned_tds:
        print(" | ".join(cleaned_tds))
