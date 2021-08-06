#Used to find and print tags and styles from the website.

from bs4 import BeautifulSoup
import requests

url="https://uem.edu.in/uem-jaipur/"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
print(soup.find_all('div'))
print(soup.find_all('style'))
print(soup.find_all('img'))
print(soup.find_all('i'))