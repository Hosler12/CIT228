from fileinput import close
import json, os

glossary = {'Dictionary':'A storage of key: value pairs',
    'List':'A storage for multiple single values, separated by a comma.',
    'F-string':'A string with an f preceding it that allows variables to be called using {}.',
    'Append':'The function that adds an item to the end of a list or string.',
    'Index':'The specific location of an item in a list or string.',
    'Print':'The function that writes a statement in the console.',
    'Function':'Something that completes a specific action, usually based on inputs.',
    'Insert':'The function that adds an item to a specified location.',
    'Del':'The function that deletes a specific item.',
    'Sorted':'A function that allows you to see a list sorted without actually changing the list.'}

filename = 'Chapter10/glossary.json'
def writeFile():
    with open(filename, 'w') as f:
        json.dump(glossary, f)

def printFile():
    with open(filename) as f:
        try:
            temp = json.load(f)
            for k,v in temp.items():
                print(f'{k} : {v}')
        except:
            print('File has not yet been made')

def appendFile():
    with open(filename) as f:
        temp = json.load(f)

    with open(filename,'w') as f:
        term = {input('Name: '):input('Definition: ')}
        temp.update(term)
        json.dump(temp,f)

while True:
    choice = input('1) Create base file 2) Print file 3) Append file 4) quit: ')
    if choice == '1':
        writeFile()
    elif choice == '2':
        printFile()
    elif choice == '3':
        appendFile()
    elif choice == '4':
        break
    else:
        print('Please enter a valid option')