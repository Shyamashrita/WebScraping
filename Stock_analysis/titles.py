#Used to find and print tittle of the website.

from bs4 import BeautifulSoup
import requests

url="https://uem.edu.in/uem-jaipur/"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
print(soup.title)