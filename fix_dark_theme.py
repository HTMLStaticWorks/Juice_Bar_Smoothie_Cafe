import os
import glob
import re

new_colors = """
                    "colors": {
                        "primary": "#16a34a",
                        "inverse-primary": "#4ade80",
                        "primary-container": "#dcfce7",
                        "on-primary-container": "#14532d",
                        "primary-fixed-dim": "#4ade80",
                        
                        "surface": "#ffffff",
                        "background": "#0f172a",
                        
                        "on-surface": "#0f172a",
                        "inverse-on-surface": "#f8fafc",
                        "on-background": "#f8fafc",
                        
                        "on-surface-variant": "#475569",
                        "outline-variant": "#94a3b8",
                        
                        "surface-container-highest": "#f1f5f9",
                        "inverse-surface": "#1e293b",
                        
                        "surface-variant": "#f1f5f9",
                        "surface-container-low": "#ffffff",
                        "surface-container": "#f8fafc",
                        
                        "secondary": "#ea580c",
                        "secondary-container": "#ffedd5",
                        "on-secondary-container": "#9a3412",
                        
                        "tertiary": "#db2777",
                        "tertiary-container": "#fce7f3",
                        "on-tertiary-container": "#9d174d",
                        
                        "on-primary": "#ffffff",
                        "on-secondary": "#ffffff",
                        "on-tertiary": "#ffffff",
                        
                        "error": "#dc2626",
                        "on-error": "#ffffff",
                        "error-container": "#fee2e2",
                        "on-error-container": "#991b1b"
                    }
"""

new_css = """
        body {
            background-color: theme('colors.surface');
            color: theme('colors.on-surface');
        }
        
        .dark body {
            background-color: theme('colors.background');
            color: theme('colors.inverse-on-surface');
        }
"""

html_files = glob.glob('*.html')
colors_pattern = r'"colors"\s*:\s*\{[^{}]*\}'
css_pattern = r'body\s*\{\s*background-color:\s*theme\(\'colors\.background\'\);\s*color:\s*theme\(\'colors\.on-background\'\);\s*\}'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update colors
    content = re.sub(colors_pattern, new_colors.strip(), content)
    
    # Update body CSS
    content = re.sub(css_pattern, new_css.strip(), content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")
