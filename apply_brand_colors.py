import glob
import re

new_colors = """
                    "colors": {
                        "primary": "#6DBE45",
                        "inverse-primary": "#6DBE45",
                        "primary-container": "#dff0d6",
                        "on-primary-container": "#1e3b10",
                        "primary-fixed-dim": "#6DBE45",
                        
                        "surface": "#FFF7E6",
                        "background": "#121a11",
                        
                        "on-surface": "#1a2418",
                        "inverse-on-surface": "#FFF7E6",
                        "on-background": "#FFF7E6",
                        
                        "on-surface-variant": "#475941",
                        "outline-variant": "#9ba696",
                        
                        "surface-container-highest": "#f2ead8",
                        "inverse-surface": "#1b261a",
                        
                        "surface-variant": "#f2ead8",
                        "surface-container-low": "#ffffff",
                        "surface-container": "#fffbf0",
                        
                        "secondary": "#F47B35",
                        "secondary-container": "#fde4d7",
                        "on-secondary-container": "#5c2a0b",
                        
                        "tertiary": "#F47B35",
                        "tertiary-container": "#fde4d7",
                        "on-tertiary-container": "#5c2a0b",
                        
                        "on-primary": "#ffffff",
                        "on-secondary": "#ffffff",
                        "on-tertiary": "#ffffff",
                        
                        "error": "#dc2626",
                        "on-error": "#ffffff",
                        "error-container": "#fee2e2",
                        "on-error-container": "#991b1b"
                    }
"""

html_files = glob.glob('*.html')
colors_pattern = r'"colors"\s*:\s*\{[^{}]*\}'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update colors
    content = re.sub(colors_pattern, new_colors.strip(), content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")
