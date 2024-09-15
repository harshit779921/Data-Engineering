import requests
from bs4 import BeautifulSoup

def fetch_and_save_to_file(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)
    return r.text  # Return the HTML content

url = "https://ggnindia.dronacharya.info/"
html_content = fetch_and_save_to_file(url, "BeautifulSoup/DCE.html")

soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())
# divs = soup.select("div.KzD1HZ")
# for div in divs:
#     print(div.string)