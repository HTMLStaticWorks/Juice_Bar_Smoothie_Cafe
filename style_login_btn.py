import os

def style_login_as_button():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    target = '<a class="font-label-md text-label-md text-primary dark:text-inverse-primary hover:scale-105 transition-transform duration-200 inline-block" href="login.html">Login</a>'
    
    replacement = '<a class="font-label-md text-label-md border-2 border-primary text-primary dark:border-primary-fixed dark:text-primary-fixed px-6 py-1.5 rounded-full hover:bg-primary hover:text-on-primary dark:hover:bg-primary-fixed dark:hover:text-on-primary-fixed hover:scale-105 transition-all duration-200 inline-block" href="login.html">Login</a>'

    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if target in content:
            content = content.replace(target, replacement)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Styled login as button in {file}")

if __name__ == '__main__':
    style_login_as_button()
