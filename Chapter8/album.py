def make_album(name,title,count = 0):
    return {'name':name,'title':title,'song count':count}

while True:
    print('Please give the following information, or enter q as the name to quit')
    n = input('What is the artist name? ')
    if n == 'q':
        break
    t = input('What is the album title? ')
    c = input('How many songs are on the album? ')
    try:
        if int(c) > 0:
            print(make_album(n,t,c))
        else:
            print(make_album(n,t))
    except:
        print(make_album(n,t))