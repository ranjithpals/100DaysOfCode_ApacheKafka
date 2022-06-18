# Import faker module used to generate fake data
from faker import Faker
from datetime import datetime as dt
from collections import defaultdict, Counter
import random


# Create Mock CreditCard Numbers and corresponding security code
def createCard_SecurityCode(num_cards: int, mock):
    # Create an dictionary of card numbers and security code
    card_code = {}
    for _ in range(0, num_cards):
        card_code[mock.credit_card_number()] = fake.credit_card_security_code()
    return card_code


# Credit Card Mock data
class FakeCreditCardData:
    # Initialize the object
    def __init__(self, card_type, card_num, security_code, trans_ts):
        self._card_num = card_num
        self._security_code = security_code
        self._card_type = card_type
        self._trans_ts = trans_ts

    # Representation of Object
    def __repr__(self):
        return f'Card Type: {self._card_type.split(" ",1)[0]}, Card Number: {self._card_num} \n \
               security_code: {self._security_code}, Transaction_timestamp: {self._trans_ts}'


if __name__ == '__main__':
    # Create a faker object
    fake = Faker()
    # Generate card number and security code details
    card_security = createCard_SecurityCode(10, fake)
    # Create a DefaultDict to count the occurrences of same card
    customers = defaultdict(int)
    count = 0
    while True:  # count < 50:
        # Derive Card Number
        # print(list(card_security.items()))
        cc_number = random.choice(list(card_security.keys()))
        customer = FakeCreditCardData(fake.credit_card_provider('visa'),
                                      cc_number,
                                      card_security[cc_number],
                                      fake.credit_card_expire
                                      (start='now', end='+10s', date_format="%m-%d-%y %H:%M:%S"))
        print(customer)
        # Accumulate the objects created
        customers[cc_number] += 1
        count += 1

    # print(Counter(customers))  # .most_common(2)
'''
# Output of the above code
# Card Type: VISA 16 digit, Card Number: 561957897714 
# security_code: 362, Transaction_timestamp: 06-17-22 01:51:22
'''