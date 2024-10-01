# 09.2.py
# download all internal files

import os

from urllib.request import urlretrieve, urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup

download_dir = "download"
base_url = "https://pythonscraping.com/"
base_netloc = urlparse(base_url).netloc


def get_abs_url(source):
    if urlparse(base_url).netloc == "":
        return base_url + source
    return source


def get_download_path(file_url):
    parsed = urlparse(file_url)
    netloc = parsed.netloc.strip("/")
    path = parsed.path.strip("/")
    local_file = f"{download_dir}/{netloc}/{path}"

    local_path = "/".join(local_file.split("/")[:-1])
    if not os.path.exists(local_path):
        os.makedirs(local_path)
    return local_file


bs = BeautifulSoup(urlopen(base_url), "html.parser")
download_list = bs.find_all(src=True)

for download in download_list:
    file_url = get_abs_url(download["src"])
    if file_url is not None:
        try:
            urlretrieve(file_url, get_download_path(file_url))
            print(file_url)
        except Exception as e:
            print(f"Could not retrieve {file_url} Error: {e}")