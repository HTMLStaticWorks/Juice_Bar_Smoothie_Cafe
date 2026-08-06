from bs4 import BeautifulSoup
import os

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
soup = BeautifulSoup(content, 'html.parser')

for a in soup.find_all('a'):
    if a.get('href') == 'services.html' and not a.text.strip():
        a.string = 'Services'

# Desktop
desktop_ul = soup.find('ul', class_=lambda c: c and 'gap-gutter' in c)
if desktop_ul:
    home2_li = None
    home_li = None
    for li in desktop_ul.find_all('li', recursive=False):
        a = li.find('a')
        if a and a.get('href') == 'about.html': home2_li = li
        if a and a.get('href') == 'index.html': home_li = li
    if home2_li and home_li:
        home2_li.extract()
        home_li.insert_after(home2_li)

# Mobile
mobile_nav = soup.find('nav', class_=lambda c: c and 'overflow-y-auto' in c)
if mobile_nav:
    home2_a = None
    home_a = None
    for a in mobile_nav.find_all('a', recursive=False):
        if a.get('href') == 'about.html': home2_a = a
        if a.get('href') == 'index.html': home_a = a
    if home2_a and home_a:
        home2_a.extract()
        home_a.insert_after(home2_a)

# Footer
footer = soup.find('footer')
if footer:
    home2_f = footer.find('a', href='about.html')
    menu_f = footer.find('a', href='menu.html')
    if home2_f and menu_f:
        home2_f.extract()
        menu_f.insert_before(home2_f)

with open('services_test.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Tested")
