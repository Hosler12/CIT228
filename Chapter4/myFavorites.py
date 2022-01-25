print('Section 1')

foods = ['pizza','yogurt','pie','hamburger','spaghetti','goulash']
numbers = [10,3,5,0,13,38]
movies = ['free guy','black panther','venom']
combo = [foods[0],foods[1],numbers[0],numbers[1],movies[0],movies[1]]
print(foods)
print(numbers)
print(movies)
print(combo)
print(foods[-1])
print(f'{numbers[1]} {numbers[3]} {numbers[5]}')
print(f'{movies[0]} {movies[1]} {movies[2]}')
print(f'{combo[0]} {combo[2]} {combo[4]}')

print('Section 2')

movies.append('captain america: civil war')
print(movies)
numbers.insert(3,7)
print(numbers)
foods.insert(5,'banana bread')
print(foods)
del foods[1]
print(foods)
numbers.pop()
print(numbers)
numbers.pop(2)
print(numbers)

print('Section 3')

movies.sort()
print(movies)
foods.sort()
print(foods)
print(sorted(numbers))
print(numbers)
movies.reverse()
print(movies)

print('Chapter 4')

for i in foods:
    print(i)
for i in numbers:
    print(i)
for i in movies:
    print(i)
for i in combo:
    print(i)