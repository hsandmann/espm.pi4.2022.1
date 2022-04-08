import requests
import db

uri = 'https://www.investopedia.com/tech/most-important-cryptocurrencies-other-than-bitcoin/'
r = requests.get(uri)
txt = r.text

i = txt.find('mntl-sc-block-table__table')
i = txt.find('tbody', i)
f = txt.find('/tbody', i)
# Limpou o texto original
txt = txt[i:f]
next_otr = txt.find('<tr>')
i = 0
coins = []
while next_otr > 0:
    next_ctr = txt.find('</tr>', next_otr)
    trechos = txt[next_otr:next_ctr].split('<td>')
    t_name = trechos[1].replace('</td>', '').replace('</a', '')
    if t_name.find('>') >= 0:
        t_name = t_name[t_name.find('>') + 1:].replace('>', '')
    name = t_name.strip()
    ticker = trechos[2].replace('</td>', '').strip()
    price = trechos[3].replace('</td>', '').replace('$', '').strip()
    coins.append([name, ticker, price])
    next_otr = txt.find('<tr>', next_otr + 1)
    # break

for c in coins:
    d = {
        'name': c[0],
        'ticker': c[1],
        'price': float(c[2])
    }
    db.insertCoin(d)