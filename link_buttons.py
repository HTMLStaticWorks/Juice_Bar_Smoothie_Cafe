from bs4 import BeautifulSoup
import os

files = ['index.html', 'menu.html', 'services.html', 'about.html', 'gallery.html', 'blog.html', 'contact.html', 'login.html', 'register.html']

for filename in files:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    # We want to change navigation buttons to links.
    # The buttons we want to change are either 'Login', 'Sign Up', or 'Sign Up Now'.
    # Note: we shouldn't change the actual form submit buttons on login.html/register.html!
    # Let's check if the button is a form submit button.
    # Form submit buttons usually have type="submit" or are inside a <form>.
    for btn in soup.find_all('button'):
        text = btn.get_text(strip=True)
        is_form_btn = btn.find_parent('form') is not None
        
        if is_form_btn:
            continue
            
        if text == 'Login':
            btn.name = 'a'
            btn['href'] = 'login.html'
            classes = btn.get('class', [])
            if 'inline-block' not in classes:
                classes.append('inline-block')
            btn['class'] = classes
            
        elif text == 'Sign Up' or text == 'Sign Up Now':
            btn.name = 'a'
            btn['href'] = 'register.html'
            classes = btn.get('class', [])
            if 'w-full' in classes:
                if 'block' not in classes: classes.append('block')
                if 'text-center' not in classes: classes.append('text-center')
            else:
                if 'inline-block' not in classes: classes.append('inline-block')
            btn['class'] = classes

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup).replace("</main></body></html>", "\n</main>\n</body>\n</html>"))

print("Buttons linked")
