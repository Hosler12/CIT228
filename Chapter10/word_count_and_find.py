from re import search


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def find_words(filename,search):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read().lower()
    except FileNotFoundError:
        pass
    else:
        words = contents.count(search)
        print(f"The file {filename} has the word '{search}' {words} times.")

filenames = ['Chapter10/valentine.txt', 'Chapter10/cagedBird.txt', 'Chapter10/liftEveryVoiceAndSing.txt']
for filename in filenames:
    count_words(filename)
searchTerm = input('Please enter your search word: ').lower()
for filename in filenames:
    find_words(filename,searchTerm)
