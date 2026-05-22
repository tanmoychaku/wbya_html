import re
with open(r"C:\Users\mrinm\.gemini\antigravity-ide\brain\cbaab472-bd8d-4128-bc31-b20825e8fc95\.system_generated\steps\170\content.md", "r", encoding="utf-8") as f:
    html = f.read()

td_contents = re.findall(r'<td[^>]*>(.*?)</td>', html, re.DOTALL)
for item in td_contents:
    text = re.sub(r'<[^>]+>', '', item).strip()
    text = text.replace('&nbsp;', '').strip()
    if text and text != 'to 2':
        print(text)
