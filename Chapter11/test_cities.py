import unittest, city_functions as cf

class test_city_country(unittest.TestCase):
    def test_city_country(self):
        toFormat = cf.formattedCity('satiago','chile')
        self.assertEqual(toFormat, 'satiago, chile - Population 0')

    def test_city_country_population(self):
        toFormat = cf.formattedCity('satiago','chile','5000000')
        self.assertEqual(toFormat, 'satiago, chile - Population 5000000')

if __name__ == '__main__':
    unittest.main()