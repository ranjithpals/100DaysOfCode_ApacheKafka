# Credit Card transaction mock data generator
import json
from collections import namedtuple


# Extract the Credit Card Provider from the faker credit_card_provider method
def extract_card_provider(card_provider_full_description: str) -> str:
    provider_name = card_provider_full_description.split(" ")[0]
    return provider_name


# Create Mock CreditCard Numbers and corresponding security code
def createCard_details(num_cards: int, mock) -> dict:
    # Create an dictionary of card numbers and security code
    card_code = {}
    for _ in range(0, num_cards):
        security_code = mock.credit_card_security_code()
        card_provider = extract_card_provider(mock.credit_card_provider())
        cc_details = namedtuple("cc_details", "sec_code cc_provider")
        temp_details = cc_details(security_code, card_provider)
        card_code[mock.credit_card_number()] = temp_details
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

    def convert_to_dict(self):
        # object properties are converted to key-value pairs python dictionary object
        return self.__dict__

    def json_serialization(self):
        # json.dumps() function converts a Python object (dictionary) into string and stores it in json_string.
        # Equivalent json string of input dictionary:
        return json.dumps(self.convert_to_dict())

# Output of json_serialization method - message stored in Kafka Topic
# {"_card_type": "VISA 16 digit", "_card_num": "561957897714"
# "_security_code": "362", "_trans_ts": "06-17-22 01:51:22"}
