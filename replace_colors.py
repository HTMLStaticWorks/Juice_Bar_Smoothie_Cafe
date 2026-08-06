import os
import glob
import re

new_colors = """
                    "colors": {
                        "primary": "#4ade80",
                        "on-primary": "#052e16",
                        "primary-container": "#dcfce7",
                        "on-primary-container": "#14532d",
                        "secondary": "#facc15",
                        "on-secondary": "#422006",
                        "secondary-container": "#fef08a",
                        "on-secondary-container": "#713f12",
                        "tertiary": "#f472b6",
                        "on-tertiary": "#500724",
                        "tertiary-container": "#fce7f3",
                        "on-tertiary-container": "#831843",
                        "background": "#ffffff",
                        "on-background": "#1e293b",
                        "surface": "#f8fafc",
                        "on-surface": "#1e293b",
                        "surface-variant": "#f1f5f9",
                        "on-surface-variant": "#334155",
                        "outline": "#cbd5e1",
                        "outline-variant": "#e2e8f0",
                        "inverse-surface": "#0f172a",
                        "inverse-on-surface": "#f8fafc",
                        "inverse-primary": "#16a34a",
                        "surface-container": "#f1f5f9",
                        "surface-container-high": "#e2e8f0",
                        "surface-container-highest": "#cbd5e1",
                        "surface-container-low": "#f8fafc",
                        "surface-container-lowest": "#ffffff",
                        "surface-bright": "#ffffff",
                        "surface-dim": "#e2e8f0",
                        "surface-tint": "#22c55e",
                        "error": "#ef4444",
                        "on-error": "#ffffff",
                        "error-container": "#fee2e2",
                        "on-error-container": "#7f1d1d",
                        "primary-fixed": "#bbf7d0",
                        "primary-fixed-dim": "#86efac",
                        "on-primary-fixed": "#064e3b",
                        "on-primary-fixed-variant": "#065f46",
                        "secondary-fixed": "#fef08a",
                        "secondary-fixed-dim": "#fde047",
                        "on-secondary-fixed": "#422006",
                        "on-secondary-fixed-variant": "#713f12",
                        "tertiary-fixed": "#fbcfe8",
                        "tertiary-fixed-dim": "#f9a8d4",
                        "on-tertiary-fixed": "#500724",
                        "on-tertiary-fixed-variant": "#831843"
                    }
"""

html_files = glob.glob('*.html')
pattern = r'"colors"\s*:\s*\{[^{}]*\}'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(pattern, new_colors.strip(), content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
