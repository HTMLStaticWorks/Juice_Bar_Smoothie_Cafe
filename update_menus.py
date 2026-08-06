import os
import re

desktop_links_li = """
<li><a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 block py-2" href="index.html">Home</a></li>
<li><a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 block py-2" href="menu.html">Menu</a></li>
<li><a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 block py-2" href="services.html">Services</a></li>
<li><a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 block py-2" href="about.html">About</a></li>
<li><a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 block py-2" href="gallery.html">Gallery</a></li>
<li><a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 block py-2" href="blog.html">Blog</a></li>
<li><a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 block py-2" href="contact.html">Contact</a></li>
"""

desktop_links_a = """
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors font-label-md text-label-md" href="index.html">Home</a>
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors font-label-md text-label-md" href="menu.html">Menu</a>
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors font-label-md text-label-md" href="services.html">Services</a>
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors font-label-md text-label-md" href="about.html">About</a>
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors font-label-md text-label-md" href="gallery.html">Gallery</a>
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors font-label-md text-label-md" href="blog.html">Blog</a>
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors font-label-md text-label-md" href="contact.html">Contact</a>
"""

mobile_links = """
<a class="flex items-center gap-4 text-on-surface-variant dark:text-outline-variant px-4 py-3 mx-2 hover:bg-surface-variant dark:hover:bg-on-surface-variant/10 rounded-xl transition-colors" href="index.html">
<span class="material-symbols-outlined">home</span>
                Home
            </a>
<a class="flex items-center gap-4 text-on-surface-variant dark:text-outline-variant px-4 py-3 mx-2 hover:bg-surface-variant dark:hover:bg-on-surface-variant/10 rounded-xl transition-colors" href="menu.html">
<span class="material-symbols-outlined">restaurant_menu</span>
                Menu
            </a>
<a class="flex items-center gap-4 text-on-surface-variant dark:text-outline-variant px-4 py-3 mx-2 hover:bg-surface-variant dark:hover:bg-on-surface-variant/10 rounded-xl transition-colors" href="services.html">
<span class="material-symbols-outlined">event_repeat</span>
                Services
            </a>
<a class="flex items-center gap-4 text-on-surface-variant dark:text-outline-variant px-4 py-3 mx-2 hover:bg-surface-variant dark:hover:bg-on-surface-variant/10 rounded-xl transition-colors" href="about.html">
<span class="material-symbols-outlined">info</span>
                About
            </a>
<a class="flex items-center gap-4 text-on-surface-variant dark:text-outline-variant px-4 py-3 mx-2 hover:bg-surface-variant dark:hover:bg-on-surface-variant/10 rounded-xl transition-colors" href="gallery.html">
<span class="material-symbols-outlined">photo_library</span>
                Gallery
            </a>
<a class="flex items-center gap-4 text-on-surface-variant dark:text-outline-variant px-4 py-3 mx-2 hover:bg-surface-variant dark:hover:bg-on-surface-variant/10 rounded-xl transition-colors" href="blog.html">
<span class="material-symbols-outlined">article</span>
                Blog
            </a>
<a class="flex items-center gap-4 text-on-surface-variant dark:text-outline-variant px-4 py-3 mx-2 hover:bg-surface-variant dark:hover:bg-on-surface-variant/10 rounded-xl transition-colors" href="contact.html">
<span class="material-symbols-outlined">contact_support</span>
                Contact
            </a>
"""

for filename in os.listdir('.'):
    if not filename.endswith('.html'):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop nav with <ul>
    ul_pattern = re.compile(r'(<ul[^>]*>)(.*?)(</ul>)', re.DOTALL)
    def repl_ul(m):
        # Only replace if it contains menu links
        if 'menu.html' in m.group(2) or 'contact.html' in m.group(2):
            return m.group(1) + "\n" + desktop_links_li.strip() + "\n" + m.group(3)
        return m.group(0)
    
    content = ul_pattern.sub(repl_ul, content)

    # Desktop nav with <nav> ... <a>...</a> </nav> where class contains "flex gap-6 items-center"
    nav_pattern = re.compile(r'(<nav class="flex gap-6 items-center">)(.*?)(</nav>)', re.DOTALL)
    content = nav_pattern.sub(lambda m: m.group(1) + "\n" + desktop_links_a.strip() + "\n" + m.group(3), content)
    
    # Mobile nav
    # The mobile nav links are inside <nav class="flex-1 overflow-y-auto..."> or inside <div class="flex flex-col gap-2"> or <nav class="flex flex-col gap-2"> depending on the file.
    # A safer way to replace mobile nav is to find the block of <a> tags that have menu.html and contact.html
    mobile_pattern1 = re.compile(r'(<nav class="flex-1 overflow-y-auto[^>]*>)(.*?)(<div class="mt-8 pt-4 border-t[^>]*>)', re.DOTALL)
    def repl_mob1(m):
        return m.group(1) + "\n" + mobile_links.strip() + "\n" + m.group(3)
    content = mobile_pattern1.sub(repl_mob1, content)
    
    mobile_pattern2 = re.compile(r'(<div class="flex flex-col gap-2">)(.*?)(</div>\s*</div>\s*</nav>)', re.DOTALL)
    def repl_mob2(m):
        if 'menu.html' in m.group(2):
            return m.group(1) + "\n" + mobile_links.strip() + "\n" + m.group(3)
        return m.group(0)
    content = mobile_pattern2.sub(repl_mob2, content)

    mobile_pattern3 = re.compile(r'(<nav class="flex flex-col gap-2">)(.*?)(</nav>)', re.DOTALL)
    def repl_mob3(m):
        if 'menu.html' in m.group(2):
            return m.group(1) + "\n" + mobile_links.strip() + "\n" + m.group(3)
        return m.group(0)
    content = mobile_pattern3.sub(repl_mob3, content)

    # Note: I need to handle footer menus later maybe, but the user specifically mentioned "website menu... based on the pages edit the menu sections to the website" which implies main navigation.

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated links")
