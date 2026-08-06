import glob
import re

new_colors_config = """
                    "colors": {
                        "primary": "var(--color-primary)",
                        "inverse-primary": "var(--color-inverse-primary)",
                        "primary-container": "var(--color-primary-container)",
                        "on-primary-container": "var(--color-on-primary-container)",
                        "primary-fixed-dim": "var(--color-primary-fixed-dim)",
                        "surface": "var(--color-surface)",
                        "background": "var(--color-background)",
                        "on-surface": "var(--color-on-surface)",
                        "inverse-on-surface": "var(--color-inverse-on-surface)",
                        "on-background": "var(--color-on-background)",
                        "on-surface-variant": "var(--color-on-surface-variant)",
                        "outline-variant": "var(--color-outline-variant)",
                        "surface-container-highest": "var(--color-surface-container-highest)",
                        "inverse-surface": "var(--color-inverse-surface)",
                        "surface-variant": "var(--color-surface-variant)",
                        "surface-container-low": "var(--color-surface-container-low)",
                        "surface-container": "var(--color-surface-container)",
                        "secondary": "var(--color-secondary)",
                        "secondary-container": "var(--color-secondary-container)",
                        "on-secondary-container": "var(--color-on-secondary-container)",
                        "tertiary": "var(--color-tertiary)",
                        "tertiary-container": "var(--color-tertiary-container)",
                        "on-tertiary-container": "var(--color-on-tertiary-container)",
                        "on-primary": "var(--color-on-primary)",
                        "on-secondary": "var(--color-on-secondary)",
                        "on-tertiary": "var(--color-on-tertiary)",
                        "error": "var(--color-error)",
                        "on-error": "var(--color-on-error)",
                        "error-container": "var(--color-error-container)",
                        "on-error-container": "var(--color-on-error-container)"
                    }
"""

css_vars_injected = """<style>
:root {
    --color-primary: #6DBE45;
    --color-inverse-primary: #6DBE45;
    --color-primary-container: #dff0d6;
    --color-on-primary-container: #1e3b10;
    --color-primary-fixed-dim: #6DBE45;
    --color-surface: #FFF7E6;
    --color-background: #FFF7E6;
    --color-on-surface: #1a2418;
    --color-inverse-on-surface: #FFF7E6;
    --color-on-background: #1a2418;
    --color-on-surface-variant: #475941;
    --color-outline-variant: #9ba696;
    --color-surface-container-highest: #f2ead8;
    --color-inverse-surface: #1b261a;
    --color-surface-variant: #f2ead8;
    --color-surface-container-low: #ffffff;
    --color-surface-container: #fffbf0;
    --color-secondary: #F47B35;
    --color-secondary-container: #fde4d7;
    --color-on-secondary-container: #5c2a0b;
    --color-tertiary: #F47B35;
    --color-tertiary-container: #fde4d7;
    --color-on-tertiary-container: #5c2a0b;
    --color-on-primary: #ffffff;
    --color-on-secondary: #ffffff;
    --color-on-tertiary: #ffffff;
    --color-error: #dc2626;
    --color-on-error: #ffffff;
    --color-error-container: #fee2e2;
    --color-on-error-container: #991b1b;
}

.dark {
    --color-primary: #6DBE45;
    --color-inverse-primary: #6DBE45;
    --color-primary-container: #1e3b10;
    --color-on-primary-container: #dff0d6;
    --color-primary-fixed-dim: #6DBE45;
    --color-surface: #121a11;
    --color-background: #121a11;
    --color-on-surface: #FFF7E6;
    --color-inverse-on-surface: #1a2418;
    --color-on-background: #FFF7E6;
    --color-on-surface-variant: #aebfa7;
    --color-outline-variant: #475941;
    --color-surface-container-highest: #1f2e1e;
    --color-inverse-surface: #FFF7E6;
    --color-surface-variant: #1f2e1e;
    --color-surface-container-low: #0a0f09;
    --color-surface-container: #182417;
    --color-secondary: #F47B35;
    --color-secondary-container: #5c2a0b;
    --color-on-secondary-container: #fde4d7;
    --color-tertiary: #F47B35;
    --color-tertiary-container: #5c2a0b;
    --color-on-tertiary-container: #fde4d7;
    --color-on-primary: #ffffff;
    --color-on-secondary: #ffffff;
    --color-on-tertiary: #ffffff;
    --color-error: #ef4444;
    --color-on-error: #ffffff;
    --color-error-container: #991b1b;
    --color-on-error-container: #fee2e2;
}
"""

html_files = glob.glob('*.html')
colors_pattern = r'"colors"\s*:\s*\{[^{}]*\}'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update tailwind config to use variables
    content = re.sub(colors_pattern, new_colors_config.strip(), content)
    
    # Inject CSS variables into the style block
    # We only inject if it's not already there
    if ':root {' not in content:
        content = content.replace('<style>', css_vars_injected)
    else:
        # If we need to replace existing root vars, we can do a regex block replacement
        # But this is the first time we're doing it, so we're safe.
        pass
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")
