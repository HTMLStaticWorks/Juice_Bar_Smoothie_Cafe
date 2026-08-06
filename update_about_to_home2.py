import os
import re

for filename in os.listdir('.'):
    if not filename.endswith('.html'):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop nav
    content = re.sub(r'href="about\.html">About</a>', r'href="about.html">Home 2</a>', content)
    
    # Mobile nav
    # The text might have whitespaces: \s+About\s+
    content = re.sub(r'(<span class="material-symbols-outlined"[^>]*>info</span>)\s+About\s+(</a>)', r'\1\n                Home 2\n            \2', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated About to Home 2")
