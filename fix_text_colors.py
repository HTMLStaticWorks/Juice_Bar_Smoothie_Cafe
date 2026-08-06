import os

def fix_text_colors():
    # Fix blog.html
    if os.path.exists('blog.html'):
        with open('blog.html', 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('text-primary-container', 'text-primary font-bold hover:text-primary-fixed')
        with open('blog.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed blog.html")

    # Fix menu.html
    if os.path.exists('menu.html'):
        with open('menu.html', 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('text-primary-container"', 'text-primary"')
        with open('menu.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed menu.html")

    # Fix login/register hover states
    for file in ['login.html', 'register.html']:
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            content = content.replace('hover:text-primary-container', 'hover:text-primary-fixed')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {file}")

if __name__ == '__main__':
    fix_text_colors()
