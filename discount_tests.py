import unittest
from discount_calculator import DiscountCalculator

class DiscountTests(unittest.TestCase):
    
    def setUp(self):
        self.discount = DiscountCalculator()
    
    def test_ten_percent_discount(self):
        self.assertEqual(self.discount.calculate_discount(100.00,10,'percent'), 10)
    
    def test_fifteen_percent_discount(self):
        self.assertEqual(self.discount.calculate_discount(50, 15, 'percent'),7.50)
    
    def test_ten_dollar_discount(self):
        self.assertEqual(self.discount.calculate_discount(100,10.0,'absolute'),10)