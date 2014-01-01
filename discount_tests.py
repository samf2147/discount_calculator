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
        
    def test_invalid_discount_type_error(self):
        self.assertRaises(ValueError, self.discount.calculate_discount, 60, 20, 'random string')
    
    def test_invalid_percents(self):
        #over 100% or less than 0%
        self.assertRaises(ValueError, self.discount.calculate_discount, 100, 120, 'percent')
        self.assertRaises(ValueError, self.discount.calculate_discount,100,-20,'percent')
        
        #0% is not ok, 100% is
        self.assertRaises(ValueError,self.discount.calculate_discount,30,0,'percent')
        self.assertEqual(self.discount.calculate_discount(50, 100, 'percent'), 50)
    
    def test_invalid_absolutes(self):
        #absolute discount can't be less than 0 or more than the cost of the item
        #discount of 0 is not ok, full discount is ok
        #over 100% or less than 0%
        self.assertRaises(ValueError, self.discount.calculate_discount, 70, 80, 'absolute')
        self.assertRaises(ValueError, self.discount.calculate_discount,70,-10,'absolute')
        
        #0% is not ok, 100% is
        self.assertRaises(ValueError,self.discount.calculate_discount,40,0.0,'absolute')
        self.assertEqual(self.discount.calculate_discount(60, 60, 'absolute'), 60)
        