import os
import re
from pathlib import Path

def move_theme_btn(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the mobile header theme toggle button
    theme_btn_pattern = re.compile(
        r'<button class="theme-toggle-btn text-on-surface-variant hover:text-primary transition-colors p-2 flex items-center justify-center">\s*<span class="material-symbols-outlined">dark_mode</span>\s*</button>',
        re.MULTILINE
    )
    
    if not theme_btn_pattern.search(content):
        print(f"Skipping {filepath} (mobile theme btn not found)")
        return

    # Remove it
    content = theme_btn_pattern.sub('', content)

    # Now add the theme toggle inside the sidenav, right before </nav>
    # We can use a regex to find </nav> that closes the sidenav nav
    # The sidenav nav ends just before <div class="p-6">
    
    # Or just replace the RTL toggle with RTL toggle + Theme toggle
    
    rtl_pattern = re.compile(
        r'(<button class="rtl-toggle-btn[^>]+>\s*<span class="material-symbols-outlined">swap_horiz</span>\s*Toggle RTL\s*</button>\s*)'
    )
    
    new_theme_btn = """<button class="theme-toggle-btn flex items-center gap-4 text-on-surface-variant dark:text-on-surface-variant px-4 py-3 mx-2 hover:bg-surface-variant dark:hover:bg-on-surface-variant/10 rounded-xl transition-colors w-[calc(100%-16px)] text-left font-bold">
<span class="material-symbols-outlined">dark_mode</span>
    Toggle Theme
</button>
"""
    if rtl_pattern.search(content):
        content = rtl_pattern.sub(r'\1' + new_theme_btn, content)
    else:
        print(f"RTL button not found in {filepath}, trying to find </nav> in sidenav...")
        # Fallback if RTL button doesn't exist
        # We can look for </nav> followed by <div class="p-6"> which is characteristic of the sidenav
        nav_pattern = re.compile(r'(</nav>\s*<div class="p-6">)')
        if nav_pattern.search(content):
            content = nav_pattern.sub(new_theme_btn + r'\1', content)
        else:
            print(f"Could not find insert location in {filepath}")
            return
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def main():
    directory = r"d:\project 2\Juice Bar & Smoothie Cafe"
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            move_theme_btn(os.path.join(directory, filename))

if __name__ == "__main__":
    main()
