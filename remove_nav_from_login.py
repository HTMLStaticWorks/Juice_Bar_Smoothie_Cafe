from bs4 import BeautifulSoup
import os

minimal_header_html = """
<header class="fixed top-0 left-0 w-full z-50 flex justify-between items-center px-margin-desktop h-20 bg-surface/90 backdrop-blur-md shadow-sm">
<a class="font-headline-md text-headline-md font-bold text-primary flex items-center gap-2 hover:scale-105 transition-transform duration-200" href="index.html">
<span class="material-symbols-outlined" data-icon="local_drink" data-weight="fill" style="font-variation-settings: 'FILL' 1;">local_drink</span>
            Juice Bar &amp; Smoothie Cafe
        </a>
</header>
"""
header_soup = BeautifulSoup(minimal_header_html, 'html.parser')
min_header = header_soup.find('header')

for filename in ['login.html', 'register.html']:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    # Remove existing nav, aside, footer, header
    for tag in soup.find_all(['nav', 'aside', 'footer', 'header']):
        tag.extract()
        
    # Remove menu script
    for s in soup.find_all('script'):
        if s.string and 'open-menu' in s.string:
            s.extract()
            
    # Insert minimal header
    body = soup.find('body')
    import copy
    if body and min_header:
        body.insert(0, copy.copy(min_header))
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup).replace("</main></body></html>", "\n</main>\n</body>\n</html>"))

print("Minimal header restored, full menu and footer removed.")
