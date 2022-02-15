import unittest
from restaurant import Restaurant

class test_resaurant(unittest.TestCase):
    def setUp(self):
        restaurant_name = 'Papa\'s Pizzeria'
        cuisine_type = 'Pizza'
        self.restaurant = Restaurant(restaurant_name,cuisine_type)

    def test_set_num_served(self):
        n = 5
        self.restaurant.set_number_served(n)
        self.assertEqual(self.restaurant.number_served, 5)

    def test_increment_number_served(self):
        n = 2
        self.restaurant.increment_number_served(n)
        self.assertEqual(self.restaurant.number_served, 2)

if __name__ == '__main__':
    unittest.main()