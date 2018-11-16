import pandas as pd
import pygal as pg

data = pd.read_csv("bakery.csv")
bakery = dict()

total = 0

for i in range(len(data)):
    total += 1
    if data['Item'][i] not in bakery:
        bakery[data['Item'][i]] = 1
    else:
        bakery[data['Item'][i]] += 1

bakery_chart = pg.Pie()
bakery_chart.title = 'Sell highlight'
for i in bakery:
    bakery_chart.add(i, bakery[i]/total*100)
bakery_chart.render_to_file('bakery_chart.svg')
