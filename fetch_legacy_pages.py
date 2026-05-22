import urllib.request
import re
import os
import time

def fetch_pages():
    with open('results-national-yoga-championship.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all legacy links
    links = re.findall(r'<a href="(http://www.westbengalyogaassociation.org/.*?)"', html)
    
    print(f"Found {len(links)} legacy links to download.")
    
    if not os.path.exists('legacy_pages'):
        os.makedirs('legacy_pages')

    for link in links:
        # Extract edition from URL
        match = re.search(r'/(\d+(?:st|nd|rd|th))-', link)
        if not match:
            # Fallback
            print(f"Could not extract edition from {link}")
            continue
            
        edition = match.group(1)
        filename = f"legacy_pages/{edition}.html"
        
        if os.path.exists(filename):
            print(f"Skipping {edition}, already exists.")
            continue
            
        print(f"Downloading {edition}...")
        try:
            req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                content = response.read().decode('utf-8')
                with open(filename, 'w', encoding='utf-8') as out:
                    out.write(content)
            time.sleep(1) # Be nice to the server
        except Exception as e:
            print(f"Failed to download {link}: {e}")

if __name__ == "__main__":
    fetch_pages()
