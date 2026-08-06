import os

def fix_footer_contrast():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace dark:text-outline-variant/70 with dark:text-on-surface-variant/70
        # Replace dark:text-outline-variant with dark:text-on-surface-variant
        if 'dark:text-outline-variant' in content:
            content = content.replace('dark:text-outline-variant/70', 'dark:text-on-surface-variant/70')
            content = content.replace('dark:text-outline-variant', 'dark:text-on-surface-variant')
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Fixed footer contrast in {file}")

if __name__ == '__main__':
    fix_footer_contrast()
