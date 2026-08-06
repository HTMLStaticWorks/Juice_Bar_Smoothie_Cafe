import re

# Read index.html to extract the correct colors config
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the colors block
colors_match = re.search(r'"colors"\s*:\s*\{[^{}]*\}', index_content, re.DOTALL)
if colors_match:
    correct_colors = colors_match.group(0)
    
    files_to_update = ['blog.html', 'contact.html']
    
    for file in files_to_update:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the entire colors object in the target file
        # The target file might have a huge colors block with many nested keys.
        # But wait, looking at the dump, the colors block doesn't have nested objects inside colors, just flat key-values.
        # However, it's very long. Let's use a robust regex or just find "colors": { ... }
        
        # In the dump above, the colors block ends at line 63.
        # We can regex it:
        content = re.sub(r'colors:\s*\{.*?(?=\n\s*borderRadius:)', correct_colors + ',', content, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated colors in {file}")
else:
    print("Could not extract colors block from index.html")
