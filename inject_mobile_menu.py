import os

script_to_inject = """
    <!-- Simple Interaction Script -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const mobileMenuBtn = document.getElementById('mobile-menu-btn');
            const closeMenuBtn = document.getElementById('close-menu-btn');
            const sidenav = document.getElementById('sidenav');

            function toggleMenu() {
                if (sidenav) {
                    sidenav.classList.toggle('translate-x-full');
                }
            }

            if (mobileMenuBtn && sidenav && closeMenuBtn) {
                mobileMenuBtn.addEventListener('click', toggleMenu);
                closeMenuBtn.addEventListener('click', toggleMenu);
            }
        });
    </script>
"""

def inject_mobile_menu_script():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Don't inject if it's already there
        if '<!-- Simple Interaction Script -->' not in content:
            # Inject right before </body>
            if '</body>' in content:
                content = content.replace('</body>', f'{script_to_inject}</body>')
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Injected script into {file}")

if __name__ == '__main__':
    inject_mobile_menu_script()
