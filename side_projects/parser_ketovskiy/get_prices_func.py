import requests
from bs4 import BeautifulSoup
from datetime import date

URL = 'https://bank-45.ru/page/kontakty'
req = requests.get(URL)
soup = BeautifulSoup(req.text, 'lxml') 
data_block = soup.find('div',attrs={'class': 'contacts-page-top', 
                              'data-branche': '39'})

def get_prices(data):
    cur_options = ['EUR','USD']
    cur_values = {}
    for curr in cur_options:
        val = data.find('tr', attrs={'class': curr})
        cur_values[curr] = []
        for i in val.find_all('td'):
            if len(i.text) > 3:
                cur_values[curr].append(float(   i.text.replace(',','.')))
    return cur_values

print(get_prices(data=data_block))

