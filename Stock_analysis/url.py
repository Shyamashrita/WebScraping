#Used to find and print links from the website.

from bs4 import BeautifulSoup
import requests

url="https://uem.edu.in/uem-jaipur/"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
print(soup.title)
for link in soup.find_all('a'):
    print(link.get('href'))