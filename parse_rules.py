import os

html_path = '/Users/chaku/.gemini/antigravity-ide/brain/8e601259-ebff-4215-949e-44a7ea95f821/.system_generated/steps/319/content.md'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(content.find('entry-content'))
print(content.find('entry-content clearfix'))
print(content.find('Rules &amp; Regulation'))

