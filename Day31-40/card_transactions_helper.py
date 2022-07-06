# Credit Card transaction mock data generator
import json
import random
from collections import namedtuple
from faker import Faker

# Functions to be publicly available when module is imported
__all__ = ['generate_card_details', 'generate_card_transaction']

# Create a faker object
fake = Faker()


# Extract the Credit Card Provider from the faker credit_card_provider method
def extract_card_provider(card_provider_full_description: str) -> str:
    provider_name = card_provider_full_description.split(" ")[0]
    return provider_name


# Create Mock CreditCard Numbers and corresponding security code
def generate_card_details(num_cards: int):  # -> dict:
    # Declare dictionary to hold card details
    card_details = {}
    for _ in range(0, num_cards):
        security_code = fake.credit_card_security_code()
        card_provider = extract_card_provider(fake.credit_card_provider())
        cc_details = namedtuple("cc_details", "sec_code cc_provider")
        temp_details = cc_details(security_code, card_provider)
        # print(temp_details)
        card_details[fake.credit_card_number()] = temp_details
    return card_details
    # print(card_details)


def generate_card_transaction(card_details):
    # Derive Card Number
    cc_number = random.choice(list(card_details.keys()))
    # Create the FakeCreditCardData Class object
    customer_obj = FakeCreditCardData(card_details[cc_number].cc_provider,
                                      cc_number,
                                      card_details[cc_number].sec_code,
                                      fake.credit_card_expire(start='now', end='+10s',
                                                              date_format="%m-%d-%y %H:%M:%S"))
    return customer_obj


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
        return f'Card Type: {self._card_type.split(" ", 1)[0]}, Card Number: {self._card_num} \n \
               security_code: {self._security_code}, Transaction_timestamp: {self._trans_ts}'

    def convert_to_dict(self):
        # object properties are converted to key-value pairs python dictionary object
        return self.__dict__

    def json_serialization(self):
        # json.dumps() function converts a Python object (dictionary) into string and stores it in json_string.
        # Equivalent json string of input dictionary:
        return json.dumps(self.convert_to_dict())

    @property
    def card_type(self):
        return self._card_type

# Output of json_serialization method - message stored in Kafka Topic
# {"_card_type": "VISA", "_card_num": "561957897714"
# "_security_code": "362", "_trans_ts": "06-17-22 01:51:22"}
