# will turn a Beautiful Soup parse tree into a nicely formatted Unicode string, with a separate line for each tag and each string

from bs4 import BeautifulSoup
import requests

url="https://uem.edu.in/uem-jaipur/"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
print(soup.prettify())