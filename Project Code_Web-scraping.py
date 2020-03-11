import urllib2
import bs4 as bs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://www.top500.org/list/2018/06/?page=1"
html = urllib2.urlopen(url)
soup = bs.BeautifulSoup(html, "lxml")

all_tables = soup.find_all('table')

right_table = soup.find('table', class_='table table-condensed table-striped')

A = []
B = []
C = []
D = []
E = []
F = []
G = []

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    if len(cells) == 7:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))

df = pd.DataFrame(A, columns=['Rank'])
df['Site'] = B
df['System'] = C
df['Cores'] = D
df['Rmax'] = E
df['Rpeak'] = F
df['Power'] = G

print df

# print soup.table.td.string

print(df.describe())

#ax = plt.axes()



plt.plot(df.Cores,df.Power, 'ro')

#ax.yaxis.set_major_locator(plt.NullLocator())
#ax.xaxis.set_major_formatter(plt.NullFormatter())




plt.show()