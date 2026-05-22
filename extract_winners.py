from bs4 import BeautifulSoup
import sys

def parse_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # The results are likely in a table
    tables = soup.find_all('table')
    for idx, table in enumerate(tables):
        print(f"--- Table {idx} ---")
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all(['td', 'th'])
            row_data = [col.get_text(strip=True) for col in cols]
            # Filter out empty strings
            row_data = [d for d in row_data if d]
            if row_data:
                print(" | ".join(row_data))
        print("\n")

if __name__ == '__main__':
    parse_html('47th-senior.html')
