import os
import re

def fix_mobile_header():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # We want to target the mobile header specifically.
    # The desktop header has "ZestUp" inside it. The mobile header does not.
    # Let's search for the exact block in the mobile header.
    
    target = """<div class="font-headline-md text-headline-md font-bold text-primary flex items-center gap-2">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">eco</span>
</div>"""

    replacement = """<div class="font-headline-md text-headline-md font-bold text-primary dark:text-inverse-primary flex items-center gap-2">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">eco</span>
ZestUp
</div>"""

    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if target in content:
            content = content.replace(target, replacement)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Added ZestUp to mobile header in {file}")

if __name__ == '__main__':
    fix_mobile_header()
