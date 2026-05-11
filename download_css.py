import os
import urllib.request

url = 'https://raw.githubusercontent.com/PacktPublishing/Django-5-by-Example/master/Chapter04/bookmarks/account/static/css/base.css'
out_path = 'account/static/css/base.css'

os.makedirs(os.path.dirname(out_path), exist_ok=True)
print(f"Downloading {url} to {out_path}...")
urllib.request.urlretrieve(url, out_path)
print("Download complete.")
