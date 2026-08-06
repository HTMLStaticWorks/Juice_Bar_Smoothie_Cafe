import re

script_content = """
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Theme toggling logic
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

            // RTL toggling logic
            const rtlBtns = document.querySelectorAll('.rtl-toggle-btn');
            
            // Initial check
            if (localStorage.dir === 'rtl') {
                document.documentElement.setAttribute('dir', 'rtl');
            } else {
                document.documentElement.setAttribute('dir', 'ltr');
            }

            rtlBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    const currentDir = document.documentElement.getAttribute('dir');
                    const newDir = currentDir === 'rtl' ? 'ltr' : 'rtl';
                    document.documentElement.setAttribute('dir', newDir);
                    localStorage.dir = newDir;
                });
            });
        });
    </script>
</body>
"""

buttons_html = """<body class="bg-background text-on-background min-h-screen flex flex-col font-body-md antialiased overflow-x-hidden relative">
<div class="absolute top-6 right-6 z-50 flex items-center gap-4" dir="ltr">
    <button class="theme-toggle-btn text-on-surface-variant dark:text-outline-variant hover:text-primary hover:scale-105 transition-transform duration-200">
        <span class="material-symbols-outlined text-[24px]">dark_mode</span>
    </button>
    <button class="rtl-toggle-btn text-on-surface-variant dark:text-outline-variant hover:text-primary hover:scale-105 transition-transform duration-200 font-label-md font-bold" title="Toggle RTL">
        RTL
    </button>
</div>
"""

files = ['login.html', 'register.html']
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace body tag to inject buttons right after it
    if '<div class="absolute top-6 right-6' not in content:
        content = re.sub(r'<body[^>]*>', buttons_html, content)
        
    # Replace </body> with script + </body>
    if 'document.querySelectorAll(\'.theme-toggle-btn\')' not in content:
        content = content.replace('</body>', script_content)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {file}")
