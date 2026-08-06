import urllib.request
import re

def get_unsplash_id(query):
    try:
        url = f"https://unsplash.com/s/photos/{query.replace(' ', '-')}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        # Find all photo IDs
        match = re.search(r'images\.unsplash\.com/photo-([a-zA-Z0-9\-]+)\?', html)
        if match:
            print(f"{query}: photo-{match.group(1)}")
            return match.group(1)
        else:
            print(f"No match for {query}")
    except Exception as e:
        print(f"Error for {query}: {e}")

get_unsplash_id("blood orange")
get_unsplash_id("turmeric root")
get_unsplash_id("fresh ginger")
