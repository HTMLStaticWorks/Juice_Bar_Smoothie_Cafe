from bs4 import BeautifulSoup
import os

img_html = '<img src="logo.png" alt="ZestUp Logo" class="h-8 md:h-10 w-auto object-contain">'
img_centered_html = '<img src="logo.png" alt="ZestUp Logo" class="h-12 md:h-16 w-auto object-contain mx-auto mb-2">'

files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    modified = False
    
    for a in soup.find_all('a'):
        classes = a.get('class', [])
        href = a.get('href')
        
        # Check if it's the brand link
        if 'font-headline-md' in classes and href in ['index.html', '/']:
            a.clear()
            if 'login.html' in filename or 'register.html' in filename:
                a.append(BeautifulSoup(img_centered_html, 'html.parser'))
            else:
                a.append(BeautifulSoup(img_html, 'html.parser'))
            modified = True
            
    for h2 in soup.find_all('h2'):
        classes = h2.get('class', [])
        if 'font-headline-lg-mobile' in classes and 'ZestUp' in h2.get_text():
            h2.name = 'div'
            h2.clear()
            h2.append(BeautifulSoup(img_html, 'html.parser'))
            # Remove text classes from the container
            new_classes = [c for c in classes if c not in ['font-headline-lg-mobile', 'text-headline-lg-mobile', 'font-bold', 'text-primary', 'dark:text-inverse-primary']]
            h2['class'] = new_classes
            modified = True
            
    if modified:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup).replace("</main></body></html>", "\n</main>\n</body>\n</html>"))

print("Image logo applied successfully.")
