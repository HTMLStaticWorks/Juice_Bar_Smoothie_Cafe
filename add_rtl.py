from bs4 import BeautifulSoup
import os

desktop_btn_html = """
<button class="rtl-toggle-btn text-on-surface-variant dark:text-outline-variant hover:text-primary hover:scale-105 transition-transform duration-200 font-label-md font-bold" title="Toggle RTL">
  RTL
</button>
"""

mobile_btn_html = """
<button class="rtl-toggle-btn flex items-center gap-4 text-on-surface-variant dark:text-outline-variant px-4 py-3 mx-2 hover:bg-surface-variant dark:hover:bg-on-surface-variant/10 rounded-xl transition-colors w-[calc(100%-16px)] text-left font-bold">
    <span class="material-symbols-outlined">swap_horiz</span>
    Toggle RTL
</button>
"""

script_html = """
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const rtlBtns = document.querySelectorAll('.rtl-toggle-btn');
        rtlBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                document.documentElement.dir = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl';
            });
        });
    });
</script>
"""

files = ['index.html', 'menu.html', 'services.html', 'about.html', 'gallery.html', 'blog.html', 'contact.html']

for filename in files:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    # Inject Desktop Button
    # Find the dark mode button which contains the dark_mode material symbol
    dark_mode_span = soup.find('span', string=lambda t: t and 'dark_mode' in t)
    if dark_mode_span:
        dark_btn = dark_mode_span.find_parent('button')
        if dark_btn and not soup.find(class_=lambda c: c and 'rtl-toggle-btn' in c and 'font-label-md' in c):
            d_btn_soup = BeautifulSoup(desktop_btn_html, 'html.parser')
            dark_btn.insert_after(d_btn_soup)
            
    # Inject Mobile Button
    sidenav = soup.find('aside', id='sidenav')
    if sidenav:
        nav = sidenav.find('nav')
        if nav and not sidenav.find(class_=lambda c: c and 'rtl-toggle-btn' in c and 'flex' in c):
            m_btn_soup = BeautifulSoup(mobile_btn_html, 'html.parser')
            nav.append(m_btn_soup)
            
    # Inject Script
    body = soup.find('body')
    if body and not soup.find(string=lambda t: t and 'rtlBtns.forEach' in t):
        s_soup = BeautifulSoup(script_html, 'html.parser')
        body.append(s_soup)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup).replace("</main></body></html>", "\n</main>\n</body>\n</html>"))

print("RTL toggle added to all menu sections.")
