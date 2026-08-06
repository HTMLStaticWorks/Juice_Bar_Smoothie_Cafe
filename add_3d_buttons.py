import glob
import re

html_files = glob.glob('*.html')

login_regex = re.compile(r'(<a class="[^"]*border-2 border-primary[^"]*?)(hover:scale-105 transition-all duration-200)([^"]*" href="login\.html">Login</a>)')
signup_regex = re.compile(r'(<a class="[^"]*bg-primary-container[^"]*?)(hover:scale-105 transition-transform duration-200)([^"]*" href="register\.html">Sign Up</a>)')

# The 3D classes
btn_3d_classes = "hover:-translate-y-1.5 hover:shadow-[0_6px_0_0_rgba(0,0,0,0.15)] active:-translate-y-0 active:shadow-[0_0px_0_0_rgba(0,0,0,0.15)] transition-all duration-200"

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = login_regex.sub(rf'\1{btn_3d_classes}\3', content)
    new_content = signup_regex.sub(rf'\1{btn_3d_classes}\3', new_content)
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
