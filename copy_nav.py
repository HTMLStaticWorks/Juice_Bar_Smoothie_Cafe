from bs4 import BeautifulSoup
import os
import copy

with open('index.html', 'r', encoding='utf-8') as f:
    index_soup = BeautifulSoup(f.read(), 'html.parser')

nav_desktop = index_soup.find('nav', class_=lambda c: c and 'md:flex' in c)
header_mobile = index_soup.find('header', class_=lambda c: c and 'md:hidden' in c)
aside_mobile = index_soup.find('aside', id='sidenav')
footer = index_soup.find('footer')

menu_script = None
for s in index_soup.find_all('script'):
    if s.string and 'open-menu' in s.string:
        menu_script = s
        break

for filename in ['login.html', 'register.html']:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    old_header = soup.find('header')
    if old_header: old_header.extract()
        
    old_footer = soup.find('footer')
    if old_footer: old_footer.extract()
    
    body = soup.find('body')
    if body:
        nd = copy.copy(nav_desktop)
        hm = copy.copy(header_mobile)
        am = copy.copy(aside_mobile)
        
        if nd:
            ha = nd.find('a', href='index.html')
            if ha: ha['class'] = "text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 block py-2".split()
        if am:
            ham = am.find('a', href='index.html')
            if ham: ham['class'] = "flex items-center gap-4 text-on-surface-variant dark:text-outline-variant px-4 py-3 mx-2 hover:bg-surface-variant dark:hover:bg-on-surface-variant/10 rounded-xl transition-colors".split()

        if am: body.insert(0, am)
        if hm: body.insert(0, hm)
        if nd: body.insert(0, nd)
        
        if footer: body.append(copy.copy(footer))
            
        if menu_script:
            existing = any(s.string and 'open-menu' in s.string for s in soup.find_all('script'))
            if not existing:
                body.append(copy.copy(menu_script))
                
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup).replace("</main></body></html>", "\n</main>\n</body>\n</html>"))

print("Menu copied to login and register")
