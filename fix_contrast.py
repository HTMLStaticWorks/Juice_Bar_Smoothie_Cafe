import os

def fix_contrast():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'text-secondary-fixed-dim' in content:
            # Replace the poor contrast class with text-secondary which is bright orange
            content = content.replace('text-secondary-fixed-dim', 'text-secondary')
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Fixed contrast in {file}")

if __name__ == '__main__':
    fix_contrast()
