#Used to find and print Paragraphs and headings from the website.

from bs4 import BeautifulSoup
import requests

url="https://uem.edu.in/uem-jaipur/"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
print(soup.find_all('p'))
print(soup.find_all('h2'))