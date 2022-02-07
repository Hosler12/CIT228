class Restaurant:
    def __init__(self,restaurant_name,cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f'At {self.restaurant_name}, we only have the lowest quality, authentic {self.cuisine_type} cuisine')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open for business.')

    def set_number_served(self,number):
        self.number_served = number
        print(f'{self.number_served} customers have been served.')

    def increment_number_served(self,number):
        self.number_served += number
        print(f'{self.number_served} customers have been served.')