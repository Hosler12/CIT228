import json, csv
import matplotlib.pyplot as matlib
import random as rand

# Set up variables

entity = []
vegequan= []
fruitquan= []
tEntity = []
tQuantity = []

# Set up vegetables - P1 T1

with open('CIT228/Project2/vegetable-consumption-per-capita.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)
    for row in csv_reader:
        if not row[1]:
            continue
        elif row[2] == '2012':
            entity.append(row[0])
            vegequan.append(float(row[3]))


matlib.hist(vegequan, bins=10, color="green")
matlib.ylabel("# of countries")
matlib.xlabel("Vegetable Quantity")
matlib.suptitle("Vegetable Consumption by Country")

matlib.savefig('vegetable.png')

# Set up fruits - P2 T1

with open('CIT228/Project2/fruit-consumption-per-capita.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)
    for row in csv_reader:
        if not row[1]:
            continue
        elif row[2] == '2012':
            fruitquan.append(float(row[3]))

matlib.hist(fruitquan, bins=10, color="green")
matlib.ylabel("# of countries")
matlib.xlabel("Fruit Quantity")
matlib.suptitle("Fruit Consumption by Country")

matlib.savefig('fruit.png')

matlib.clf()

# Get random entities - P3 T2

for i in range(20):
    num = rand.randint(0,len(entity)-1)
    tEntity.append(entity[num])
    tQuantity.append(vegequan[num])

matlib.scatter(tEntity, tQuantity, label="Quantity",s=50)
matlib.ylabel("Quantity")
matlib.xlabel("Entity")

matlib.xticks(rotation='vertical')

matlib.suptitle("Random Countries Vegetables Consumption")
matlib.savefig('randomVegetable.png')

matlib.clf()

# Pie of Random - P4 T3

wedgeColors=('lightgreen','purple','lavender','lemonchiffon', 'tan')

matlib.pie(tQuantity, labels=tEntity, autopct='%3.1f%%', shadow=True, startangle=-40, colors=wedgeColors)
matlib.axis('equal')
matlib.suptitle("Random pie")

matlib.savefig('randomVegetablePie.png')

matlib.clf()

# Vegetable Bars - P5 T4

matlib.bar(entity, vegequan, color ='green')
matlib.xticks(color='w')
matlib.savefig('vegetableBar.png')

matlib.clf()

# Fruit Bars - P6 T4

matlib.bar(entity, fruitquan, color ='red')
matlib.xticks(color='w')

matlib.savefig('fruitBar.png')