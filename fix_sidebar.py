import os

def fix_sidebar():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    logo_target = '<div class=""><img alt="ZestUp Logo" class="h-8 md:h-10 w-auto object-contain" src="logo.png"/></div>'
    logo_replacement = """<div class="font-headline-md text-headline-md font-bold text-primary dark:text-inverse-primary flex items-center gap-2">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">eco</span>
ZestUp
</div>"""

    buttons_target = """<div class="p-6">
<a class="w-full font-label-md text-label-md bg-primary-container text-on-primary-container py-4 rounded-xl hover:bg-surface-variant dark:hover:bg-on-surface-variant/10 transition-colors block text-center" href="register.html">
                Sign Up Now
            </a>
</div>"""
    
    buttons_replacement = """<div class="p-6">
<a class="w-full font-label-md text-label-md border-2 border-primary text-primary dark:border-primary-fixed dark:text-primary-fixed py-3 rounded-xl hover:bg-primary hover:text-on-primary transition-colors block text-center mb-3" href="login.html">
                Login
            </a>
<a class="w-full font-label-md text-label-md bg-primary-container text-on-primary-container py-3 rounded-xl hover:bg-surface-variant dark:hover:bg-on-surface-variant/10 transition-colors block text-center" href="register.html">
                Sign Up Now
            </a>
</div>"""

    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        if logo_target in content:
            content = content.replace(logo_target, logo_replacement)
            modified = True
            
        if buttons_target in content:
            content = content.replace(buttons_target, buttons_replacement)
            modified = True
            
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed sidebar in {file}")

if __name__ == '__main__':
    fix_sidebar()
