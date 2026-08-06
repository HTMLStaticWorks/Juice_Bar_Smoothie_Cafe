import os

def add_theme_btn():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    target = """<button class="text-primary p-2" id="mobile-menu-btn">
<span class="material-symbols-outlined">menu</span>
</button>"""
    
    replacement = """<div class="flex items-center gap-2">
<button class="theme-toggle-btn text-on-surface-variant hover:text-primary transition-colors p-2 flex items-center justify-center">
<span class="material-symbols-outlined">dark_mode</span>
</button>
<button class="text-primary p-2" id="mobile-menu-btn">
<span class="material-symbols-outlined">menu</span>
</button>
</div>"""

    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if target in content:
            content = content.replace(target, replacement)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added theme button to {file}")

if __name__ == '__main__':
    add_theme_btn()
