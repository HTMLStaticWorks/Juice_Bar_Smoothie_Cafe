import os
import re

for filename in os.listdir('.'):
    if not filename.endswith('.html'):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the brand name in various forms
    # Juice Bar & Smoothie Cafe
    # Juice Bar &amp; Smoothie Cafe
    # Juice Bar
    new_content = re.sub(r'Juice Bar(?:\s*(?:&|&amp;)\s*Smoothie Cafe)?', 'ZestUp', content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Brand name updated to ZestUp.")
