import os

def fix_footer_grid():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    target = '<div class="max-w-container-max mx-auto grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">'
    replacement = '<div class="max-w-container-max mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-12 mb-12">'

    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if target in content:
            content = content.replace(target, replacement)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed footer grid in {file}")

if __name__ == '__main__':
    fix_footer_grid()
