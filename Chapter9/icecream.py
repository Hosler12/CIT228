from restaurant import *

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type, flavor = [], number_served = 0):
        super().__init__(restaurant_name,cuisine_type,number_served=0)
        self.flavor = flavor

    def displayFlavors(self):
        print('The available flavors are')
        for i in self.flavor:
            print(i)