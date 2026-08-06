import os

def fix_bad_image():
    bad_url = "https://images.unsplash.com/photo-1546890975-7596e98cdbf1?q=80&w=800"
    
    replacements = {
        'services.html': [
            (bad_url, "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?q=80&w=800")
        ],
        'register.html': [
            (bad_url, "https://images.unsplash.com/photo-1517865288-9366e00cf7bc?q=80&w=800")
        ],
        'gallery.html': [
            (bad_url, "https://images.unsplash.com/photo-1505252585461-04db1eb84625?q=80&w=800")
        ],
        'contact.html': [
            (bad_url, "https://images.unsplash.com/photo-1524661135-423995f22d0b?q=80&w=800")
        ],
        'blog.html': [
            (bad_url, "https://images.unsplash.com/photo-1554118811-1e0d58224f24?q=80&w=800")
        ]
    }

    # For files with 1 occurrence, simple replace
    for file, reps in replacements.items():
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            for old, new in reps:
                content = content.replace(old, new)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {file}")

    # For menu.html, we have 2 occurrences, let's read and replace sequentially
    if os.path.exists('menu.html'):
        with open('menu.html', 'r', encoding='utf-8') as f:
            content = f.read()
            
        # First occurrence is Citrus Sunrise
        content = content.replace(bad_url, "https://images.unsplash.com/photo-1613478223719-2ab802602423?q=80&w=800", 1)
        
        # Second occurrence is Chocolate peanut butter shake
        content = content.replace(bad_url, "https://images.unsplash.com/photo-1572490122747-3968b75bf699?q=80&w=800", 1)
        
        with open('menu.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed menu.html")

if __name__ == '__main__':
    fix_bad_image()
