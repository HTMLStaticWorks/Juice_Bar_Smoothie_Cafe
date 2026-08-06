import os
import re

def audit_heroes():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find the h1 tag and grab surrounding context
        h1_matches = re.finditer(r'<h1[^>]*>.*?</h1>', content, re.DOTALL)
        print(f"\n--- {file} ---")
        for match in h1_matches:
            start = max(0, match.start() - 250)
            end = min(len(content), match.end() + 250)
            snippet = content[start:end]
            
            # Print simplified tags to analyze structure
            tags = re.findall(r'<[^>]+>', snippet)
            print(f"H1 Found: {match.group(0)}")
            print("Context tags around H1:")
            for t in tags:
                if 'class="' in t:
                    cls = re.search(r'class="([^"]+)"', t)
                    print(f"  {t.split(' ')[0]} class='{cls.group(1)}'")
                else:
                    print(f"  {t}")

if __name__ == '__main__':
    audit_heroes()
