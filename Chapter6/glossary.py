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

for k,v in glossary.items():
    print(f'{k}\n\t{v}')