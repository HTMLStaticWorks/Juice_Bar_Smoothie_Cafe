import os

def update_breakpoints():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Target the specific nav and header blocks to update breakpoints from md to lg
        if '<header class="md:hidden' in content or '<nav class="hidden md:flex' in content:
            content = content.replace('<header class="md:hidden', '<header class="lg:hidden')
            content = content.replace('<nav class="hidden md:flex', '<nav class="hidden lg:flex')
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Updated breakpoints for {file}")

if __name__ == '__main__':
    update_breakpoints()
