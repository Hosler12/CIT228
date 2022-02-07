class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'At {self.restaurant_name}, we only have the lowest quality, authentic {self.cuisine_type} cuisine')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open for business.')
    
restaurant = Restaurant('That Place','American')
print(f'The restaurant is called {restaurant.restaurant_name}')
print(f'Their cuisine consists of {restaurant.cuisine_type}')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print('\n 9-2 \n')

restaurant1 = Restaurant('That One Place','Banana')
restaurant2 = Restaurant('That Two Place','American')
restaurant3 = Restaurant('That Three Place','\'Merican')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()