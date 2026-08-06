import os
import glob
import re

html_files = glob.glob('*.html')

script_to_add = """
    <!-- Theme Toggle Script -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const themeBtns = document.querySelectorAll('.theme-toggle-btn');
            
            // Initial check
            if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }

            // Update icons based on initial state
            themeBtns.forEach(btn => {
                const icon = btn.querySelector('.material-symbols-outlined');
                if (icon) {
                    icon.textContent = document.documentElement.classList.contains('dark') ? 'light_mode' : 'dark_mode';
                }
                
                btn.addEventListener('click', () => {
                    document.documentElement.classList.toggle('dark');
                    const isDark = document.documentElement.classList.contains('dark');
                    
                    if (isDark) {
                        localStorage.theme = 'dark';
                    } else {
                        localStorage.theme = 'light';
                    }
                    
                    // Update all buttons
                    themeBtns.forEach(b => {
                        const i = b.querySelector('.material-symbols-outlined');
                        if (i) {
                            i.textContent = isDark ? 'light_mode' : 'dark_mode';
                        }
                    });
                });
            });
        });
    </script>
"""

# add tailwind darkmode config script at head if it's missing the darkMode: "class" ? 
# We saw that tailwind.config has darkMode: "class" so that's fine.

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Add class 'theme-toggle-btn' to the button containing dark_mode span
    # Pattern: <button ...> \s* <span class="material-symbols-outlined">dark_mode</span> \s* </button>
    # We will use regex to find this button and add the class.
    
    # We look for the span dark_mode first
    pattern = r'(<button\s+[^>]*?class=")([^"]*)("([^>]*?)>\s*<span\s+class="material-symbols-outlined">\s*(?:dark_mode|light_mode)\s*</span>\s*</button>)'
    
    def replacer(match):
        prefix = match.group(1)
        classes = match.group(2)
        suffix = match.group(3)
        
        if 'theme-toggle-btn' not in classes:
            classes = 'theme-toggle-btn ' + classes
        
        return prefix + classes + suffix

    new_content = re.sub(pattern, replacer, content, flags=re.IGNORECASE)
    
    if new_content != content:
        content = new_content
        modified = True
        
    # 2. Add the script before </body>
    if '<!-- Theme Toggle Script -->' not in content and 'theme-toggle-btn' in content:
        content = content.replace('</body>', script_to_add + '\n</body>')
        modified = True
        
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Done.")
