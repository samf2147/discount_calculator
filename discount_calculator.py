class DiscountCalculator():
    
    def __init__(self):
        pass
    
    def calculate_discount(self, original, discount, type):
        if type == 'percent':
            return 0.01 * original * discount
        elif type == 'absolute':
            return discount
        else:
            return None