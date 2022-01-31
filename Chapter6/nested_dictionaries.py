dictionaryDict = {1:{2:3},2:{4:8},3:{9:27}}

for k,v in dictionaryDict.items():
    print(f'{k}: {v}')

for k,v in dictionaryDict.items():
    for l,b in v.items():
        print(f'{k}: {l}: {b}')