import urllib.request
import os

images_to_download = [
    ("gallery_smoothie_1.jpg", "https://loremflickr.com/800/800/smoothie?lock=101"),
    ("gallery_juice_1.jpg", "https://loremflickr.com/800/800/juice?lock=102"),
    ("gallery_smoothie_2.jpg", "https://loremflickr.com/800/800/smoothie?lock=103"),
    ("gallery_fruit_1.jpg", "https://loremflickr.com/800/800/fruit?lock=106"),
    ("gallery_juice_2.jpg", "https://loremflickr.com/800/800/juice?lock=105"),
]

for filename, url in images_to_download:
    filepath = os.path.join("images", filename)
    print(f"Downloading {url} to {filepath}...")
    try:
        # Need a user agent because some servers block python urllib
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
