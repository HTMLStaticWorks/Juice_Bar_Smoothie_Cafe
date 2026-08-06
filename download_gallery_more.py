import urllib.request
import os

images_to_download = [
    ("gallery_smoothie_3.jpg", "https://loremflickr.com/800/800/smoothie?lock=110"),
    ("gallery_juice_3.jpg", "https://loremflickr.com/800/800/juice?lock=111"),
    ("gallery_fruit_2.jpg", "https://loremflickr.com/800/800/fruit?lock=112"),
]

for filename, url in images_to_download:
    filepath = os.path.join("images", filename)
    print(f"Downloading {url} to {filepath}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
