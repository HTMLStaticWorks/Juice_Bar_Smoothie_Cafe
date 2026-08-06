import os
import re

desktop_links_a = """
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 font-label-md text-label-md" href="index.html">Home</a>
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 font-label-md text-label-md" href="menu.html">Menu</a>
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 font-label-md text-label-md" href="services.html">Services</a>
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 font-label-md text-label-md" href="about.html">About</a>
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 font-label-md text-label-md" href="gallery.html">Gallery</a>
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 font-label-md text-label-md" href="blog.html">Blog</a>
<a class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 font-label-md text-label-md" href="contact.html">Contact</a>
"""

mobile_links_2 = """
<a class="flex flex-col items-center gap-1 text-on-surface-variant hover:text-primary transition-colors" href="index.html">
<span class="material-symbols-outlined" data-icon="home">home</span>
<span class="font-label-md text-label-md text-[10px]">Home</span>
</a>
<a class="flex flex-col items-center gap-1 text-on-surface-variant hover:text-primary transition-colors" href="menu.html">
<span class="material-symbols-outlined" data-icon="restaurant_menu">restaurant_menu</span>
<span class="font-label-md text-label-md text-[10px]">Menu</span>
</a>
<a class="flex flex-col items-center gap-1 text-on-surface-variant hover:text-primary transition-colors" href="services.html">
<span class="material-symbols-outlined" data-icon="event_repeat">event_repeat</span>
<span class="font-label-md text-label-md text-[10px]">Services</span>
</a>
<a class="flex flex-col items-center gap-1 text-on-surface-variant hover:text-primary transition-colors" href="about.html">
<span class="material-symbols-outlined" data-icon="info">info</span>
<span class="font-label-md text-label-md text-[10px]">About</span>
</a>
<a class="flex flex-col items-center gap-1 text-on-surface-variant hover:text-primary transition-colors" href="gallery.html">
<span class="material-symbols-outlined" data-icon="photo_library">photo_library</span>
<span class="font-label-md text-label-md text-[10px]">Gallery</span>
</a>
<a class="flex flex-col items-center gap-1 text-on-surface-variant hover:text-primary transition-colors" href="contact.html">
<span class="material-symbols-outlined" data-icon="location_on">location_on</span>
<span class="font-label-md text-label-md text-[10px]">Contact</span>
</a>
"""

footer_links_col = """
<a class="font-label-md text-label-md text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:translate-y-[-2px] duration-200" href="index.html">Home</a>
<a class="font-label-md text-label-md text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:translate-y-[-2px] duration-200" href="menu.html">Menu</a>
<a class="font-label-md text-label-md text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:translate-y-[-2px] duration-200" href="services.html">Services</a>
<a class="font-label-md text-label-md text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:translate-y-[-2px] duration-200" href="about.html">About</a>
<a class="font-label-md text-label-md text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:translate-y-[-2px] duration-200" href="gallery.html">Gallery</a>
<a class="font-label-md text-label-md text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:translate-y-[-2px] duration-200" href="blog.html">Blog</a>
<a class="font-label-md text-label-md text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:translate-y-[-2px] duration-200" href="contact.html">Contact</a>
"""

for filename in os.listdir('.'):
    if not filename.endswith('.html'):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Desktop Nav Block in div/nav
    # We find a block of anchors starting with "Menu" and ending with "Locations" or "Contact Us"
    pattern1 = re.compile(r'(<a[^>]+href="menu\.html"[^>]*>Menu</a>.*?)<a[^>]+href="contact\.html"[^>]*>(?:Locations|Contact|Contact Us)</a>', re.DOTALL)
    
    def repl1(m):
        # We replace the entire matched block with desktop_links_a
        # Wait, if they have different class styles, we might override them. But desktop_links_a is standard.
        # Let's keep the classes of the first anchor
        first_a = m.group(1).split('href')[0]
        # It's easier to just use desktop_links_a
        return desktop_links_a.strip()

    # 2. But we only want to do this inside <nav> or <header> or <div class="flex gap-gutter items-center">
    # Let's target the exact block in contact.html:
    # <a ...>Menu</a>
    # <a ...>Subscriptions</a>
    # <a ...>Cleanse Plans</a>
    # <a ...>Our Story</a>
    # <a ...>Locations</a>
    
    # Replace Subscriptions with Services, Our Story with About, Locations with Contact
    content = content.replace(">Subscriptions</a>", ">Services</a>")
    content = content.replace(">Cleanse Plans</a>", ">Gallery</a>") # We change cleanse plans to gallery, then we fix href later
    content = content.replace(">Our Story</a>", ">About</a>")
    content = content.replace(">Locations</a>", ">Contact</a>")
    
    # Now fix the hrefs
    content = re.sub(r'href="services\.html"[^>]*>Gallery</a>', r'href="gallery.html">Gallery</a>', content)
    
    # Add Blog if it doesn't exist?
    # This is getting messy. Let's just use regex to match the sequence of anchors and replace with the standard set.
    
    # Let's reload content to avoid mess
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find <div class="flex gap-gutter items-center"> ... </div> or <div class="flex gap-8 items-center"> or <div class="flex gap-6 items-center">
    nav_div_pattern = re.compile(r'(<div class="flex (?:gap-gutter|gap-8|gap-6) items-center">)(.*?)(</div>)', re.DOTALL)
    def repl_div(m):
        if 'menu.html' in m.group(2) and 'contact.html' in m.group(2):
            return m.group(1) + "\n" + desktop_links_a.strip() + "\n" + m.group(3)
        return m.group(0)
    content = nav_div_pattern.sub(repl_div, content)

    # Mobile nav in contact.html: <div class="md:hidden flex fixed bottom-0 left-0 w-full bg-surface-container-highest border-t border-outline-variant z-50 justify-around p-3 pb-safe shadow-2xl">
    mob_pattern = re.compile(r'(<div class="md:hidden flex fixed bottom-0 left-0[^>]*z-50 justify-around[^>]*>)(.*?)(</div>)', re.DOTALL)
    def repl_mob(m):
        if 'menu.html' in m.group(2):
            return m.group(1) + "\n" + mobile_links_2.strip() + "\n" + m.group(3)
        return m.group(0)
    content = mob_pattern.sub(repl_mob, content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated links")
