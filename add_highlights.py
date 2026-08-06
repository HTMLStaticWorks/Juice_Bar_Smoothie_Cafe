import os
import re

files_map = {
    'index.html': 'Home',
    'menu.html': 'Menu',
    'services.html': 'Services',
    'about.html': 'Home 2',
    'gallery.html': 'Gallery',
    'blog.html': 'Blog',
    'contact.html': 'Contact'
}

for filename, link_text in files_map.items():
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop
    desktop_pattern = r'class="text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:scale-105 duration-200 block py-2" href="' + re.escape(filename) + r'">' + link_text + r'</a>'
    desktop_repl = r'class="text-primary dark:text-inverse-primary font-bold hover:scale-105 duration-200 block py-2 border-b-2 border-primary" href="' + filename + '">' + link_text + '</a>'
    content = re.sub(desktop_pattern, desktop_repl, content)

    # Mobile
    mobile_pattern = r'(class="flex items-center gap-4 text-on-surface-variant dark:text-outline-variant px-4 py-3 mx-2 hover:bg-surface-variant dark:hover:bg-on-surface-variant/10 rounded-xl transition-colors" href="' + re.escape(filename) + r'">)([\s\S]*?)' + link_text + r'(\s*</a>)'
    
    def mob_repl(m):
        cls_attr = 'class="flex items-center gap-4 text-primary dark:text-inverse-primary bg-surface-variant dark:bg-on-surface-variant/10 px-4 py-3 mx-2 rounded-xl transition-colors font-bold"'
        return f'{cls_attr} href="{filename}">{m.group(2)}{link_text}{m.group(3)}'
        
    content = re.sub(mobile_pattern, mob_repl, content)

    # Footer 1
    footer_pattern_1 = r'class="font-label-md text-label-md text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-inverse-primary transition-colors hover:translate-y-\[-2px\] duration-200" href="' + re.escape(filename) + r'">' + link_text + r'(?: Us)?</a>'
    def ft_repl_1(m):
        cls_str = 'font-label-md text-label-md text-primary dark:text-inverse-primary font-bold hover:translate-y-[-2px] duration-200 transition-transform'
        text_part = m.group(0).split('>')[-1] # e.g. "Contact Us</a>"
        return f'class="{cls_str}" href="{filename}">{text_part}'
    content = re.sub(footer_pattern_1, ft_repl_1, content)
    
    # Footer 2
    footer_pattern_2 = r'class="text-on-surface-variant hover:text-primary transition-colors font-label-md text-label-md hover:translate-y-\[-2px\] duration-200" href="' + re.escape(filename) + r'">' + link_text + r'(?: Us)?</a>'
    def ft_repl_2(m):
        cls_str = 'text-primary font-bold font-label-md text-label-md hover:translate-y-[-2px] duration-200 transition-transform'
        text_part = m.group(0).split('>')[-1]
        return f'class="{cls_str}" href="{filename}">{text_part}'
    content = re.sub(footer_pattern_2, ft_repl_2, content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Highlights added")
