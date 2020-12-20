from django.db import models
from datetime import datetime,timezone;
import string;
import random;
def getPromoCode():
        '''
        generate alphanumercial string used as promo code
        '''
        alpha_numeric=string.ascii_letters + string.digits;
        random_code=''.join(random.choice(alpha_numeric) for _ in range(8));
        return random_code; 

'''
represents time now in UTC
'''
now=datetime.now(timezone.utc)