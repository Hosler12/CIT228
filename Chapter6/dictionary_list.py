lists = [{'1.1':1,'1.2':2,'1.3':3},
    {'2.1':1,'2.2':2,'2.3':3},
    {'3.1':1,'3.2':2,'3.3':3}]

for i in lists:
    print(i)

for i in lists:
    for k,v in i.items():
        print(f'{k}: {v}')