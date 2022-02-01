sandwich_orders = ['vegan','italian','steak','pastrami','pastrami','blt','pastrami']
finished_sandwiches = []

while len(sandwich_orders) > 0:
    if sandwich_orders[0] == 'pastrami':
        print('We are out of pastrami')
        del(sandwich_orders[0])
    else:
        print(sandwich_orders[0], 'sandwich made')
        finished_sandwiches.append(sandwich_orders[0])
        del(sandwich_orders[0])

print('Sandwiches made. ')
for i in finished_sandwiches:
    print(i)