from bs4 import BeautifulSoup
import os

favicon_html = '<link rel="icon" type="image/png" href="logo.png">'

files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    head = soup.find('head')
    if head:
        existing = False
        for link in head.find_all('link'):
            rel = link.get('rel')
            if rel:
                # rel can be a list or a string
                if isinstance(rel, list):
                    if any('icon' in r.lower() for r in rel):
                        existing = True
                        break
                elif isinstance(rel, str):
                    if 'icon' in rel.lower():
                        existing = True
                        break
                        
        if not existing:
            head.append(BeautifulSoup(favicon_html, 'html.parser'))
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(str(soup).replace("</main></body></html>", "\n</main>\n</body>\n</html>"))

print("Favicon added.")
