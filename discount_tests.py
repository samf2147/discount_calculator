import unittest
from discount import DiscountCalculator

class DiscountTests(unittest.TestCase):
    
    def setUp(self):
        self.discount = DiscountCalculator()
    
    def test_calculate_discount(self):
        self.assertEqual(self.discount.calculate_discount(100.00,10,'percent'), 10)
        self.assertEqual(self.discount.calculate_discount(100,10.0,'amount'),10)