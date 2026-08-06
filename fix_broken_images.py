import os
import re

unsplash_urls = [
    "https://images.unsplash.com/photo-1546890975-7596e98cdbf1?q=80&w=800", # Smoothie bowl
    "https://images.unsplash.com/photo-1556881286-fc6915169721?q=80&w=800", # Green juice
    "https://images.unsplash.com/photo-1600271886742-f049cd451bba?q=80&w=800", # Orange juice
    "https://images.unsplash.com/photo-1610832958506-aa56368176cf?q=80&w=800", # Yellow smoothie
    "https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?q=80&w=800", # Pink/red smoothie
    "https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=800", # Healthy food bowl
    "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=800", # Salad
    "https://images.unsplash.com/photo-1493770348161-369560ae357d?q=80&w=800", # Breakfast
    "https://images.unsplash.com/photo-1511690656952-34342bb7c2f2?q=80&w=800", # Food spread
    "https://images.unsplash.com/photo-1488477181946-6428a0291777?q=80&w=800", # Fruit
    "https://images.unsplash.com/photo-1540420773420-3366772f4999?q=80&w=800", # Healthy bowl
    "https://images.unsplash.com/photo-1557844352-761f2565b576?q=80&w=800", # Veggies
    "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?q=80&w=800", # Healthy pasta
    "https://images.unsplash.com/photo-1525385133512-2f3bdd039054?q=80&w=800", # Juice bottles
    "https://images.unsplash.com/photo-1622597467836-f38240662c8b?q=80&w=800", # Green smoothie
    "https://images.unsplash.com/photo-1589733955941-5eeaf752f6dd?q=80&w=800", # Citrus
]

# For abstract backgrounds
abstract_bg = "https://images.unsplash.com/photo-1557682250-33bd709cbe85?q=80&w=1920"

def fix_images():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all aida-public urls
        aida_urls = re.findall(r'https://lh3\.googleusercontent\.com/aida-public/[A-Za-z0-9_-]+', content)
        
        if not aida_urls:
            continue
            
        # Deduplicate
        aida_urls = list(set(aida_urls))
        
        url_idx = 0
        for old_url in aida_urls:
            # Check context to see if it's a background or normal image
            # If it's used in style="background-image: url('...')" we use abstract or a wide image
            if old_url in content:
                new_url = unsplash_urls[url_idx % len(unsplash_urls)]
                content = content.replace(old_url, new_url)
                url_idx += 1
                
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Fixed {len(aida_urls)} images in {file}")

if __name__ == '__main__':
    fix_images()
