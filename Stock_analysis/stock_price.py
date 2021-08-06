# to print the current price of the particular company from yahoo finance and see the updated price.

from bs4 import BeautifulSoup
import requests
import csv

def stock():
    req = requests.get('https://in.finance.yahoo.com/quote/BTC-INR?p=BTC-INR')
    soup = BeautifulSoup(req.text, 'lxml')
    price = soup.find('div', {'class': 'D(ib) Mend(20px)'}).findAll('span')
    file = csv.writer(open("output.csv", "w"))
    file.writerow([price[0].text])
    return price[0].text

while True:
    print('The current price: '+str(stock()))