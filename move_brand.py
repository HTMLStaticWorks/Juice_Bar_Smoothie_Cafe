from bs4 import BeautifulSoup
import os

brand_html = """
<a class="font-headline-md text-headline-md font-bold text-primary flex items-center justify-center gap-2 hover:scale-105 transition-transform duration-200 mb-4" href="index.html">
<span class="material-symbols-outlined text-3xl" data-icon="local_drink" data-weight="fill" style="font-variation-settings: 'FILL' 1;">local_drink</span>
    ZestUp
</a>
"""

for filename in ['login.html', 'register.html']:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    header = soup.find('header')
    if header:
        header.extract()
        
    title_div = soup.find('div', class_=lambda c: c and 'text-center' in c and 'mb-8' in c)
    if title_div:
        # Check if we already inserted it to avoid duplicates
        existing = title_div.find('a', href='index.html')
        if not existing:
            brand_soup = BeautifulSoup(brand_html, 'html.parser')
            title_div.insert(0, brand_soup)
            
            # If register has the person_add icon, maybe hide or remove it for cleaner look
            # or just leave it. Let's just leave it for now.
        
    main = soup.find('main')
    if main:
        classes = main.get('class', [])
        if 'pt-[120px]' in classes:
            classes.remove('pt-[120px]')
            main['class'] = classes
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup).replace("</main></body></html>", "\n</main>\n</body>\n</html>"))

print("Brand moved to inside the box")
