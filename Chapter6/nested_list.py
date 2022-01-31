dictionaryList = {'list1':[1,2,3],'list2':[4,5,6]}

for k,v in dictionaryList.items():
    print(f'{k}: {v}')

for k,v in dictionaryList.items():
    for i in v:
        print(f'{k}: {i}')