class DiscountCalculator():
    
    def __init__(self):
        pass
    
    def calculate_discount(self, original, discount, discount_type):
        discount_value = None
        
        #handle percent case
        if discount_type == 'percent':
            if not self._valid_percent(discount):
                raise ValueError
            else:
                discount_value = 0.01 * original * discount
                
        #handle absolute case
        elif discount_type == 'absolute':
            if not self._valid_absolute(original, discount):
                raise ValueError
            else:
                discount_value = discount
            
        #handle invalid discount type
        else:
            raise ValueError
        return discount_value
    
    def _valid_percent(self, percent):
        '''
        Returns True iff percent is between 0 and 100
        Don't allow 0% discounts or 100% discounts
        '''
        if percent > 0 and percent <= 100:
            valid = True
        else:
            valid = False
        return valid

    def _valid_absolute(self, original, discount):
        if discount > 0 and discount <= original:
            return True
        else:
            return False