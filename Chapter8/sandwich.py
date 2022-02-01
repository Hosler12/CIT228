def make_sandwich(*ingredients):
    print('You have ordered a sandwich with')
    for i in ingredients:
        print(i)

make_sandwich('salami')
make_sandwich('salami', 'mozerella')
make_sandwich('mozerella','salami','baloni')