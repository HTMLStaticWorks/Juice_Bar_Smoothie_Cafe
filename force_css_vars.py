import re
import glob

# Read the correct style block from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

style_match = re.search(r'<style>.*?</style>', index_content, re.DOTALL)
if style_match:
    correct_style = style_match.group(0)
    
    files_to_update = ['blog.html', 'contact.html']
    for file in files_to_update:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace the existing style block with the correct one
        content = re.sub(r'<style>.*?</style>', correct_style, content, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
else:
    print("Could not find style block in index.html")
