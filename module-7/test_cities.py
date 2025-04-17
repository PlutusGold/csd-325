#Dario Gomez CSD325 Assignment 7.2 function test 4/15/2025

import unittest
from city_functions import get_city_country


class test_city_country(unittest.TestCase):
    def test_spain(self):
        formated_combo = get_city_country('Madrid', 'Spain')
        self.assertEqual(formated_combo, 'Madrid, Spain')
    def test_colombia(self):
        formated_combo = get_city_country('Bogota', 'Colombia')
        self.assertEqual(formated_combo,'Bogota, Colombia')
    def test_italy(self):
        formated_combo = get_city_country('Rome', 'Italy')
        self.assertEqual(formated_combo, 'Rome, Italy')

if __name__ == '__main__':
    unittest.main()
