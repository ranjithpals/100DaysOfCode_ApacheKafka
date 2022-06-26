#!/usr/bin/env python

import random
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer
from faker import Faker
from collections import defaultdict
from mockdata_card_transactions import FakeCreditCardData, createCard_SecurityCode

if __name__ == '__main__':
    # Parse the command line.
    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'))
    args = parser.parse_args()

    # Parse the configuration.
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    config_parser = ConfigParser()
    config_parser.read_file(args.config_file)
    config = dict(config_parser['default'])

    # Create Producer instance
    producer = Producer(config)

    # Optional per-message delivery callback (triggered by poll() or flush())
    # when a message has been successfully delivered or permanently
    # failed delivery (after retries).
    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

    # Topic to write messages
    topic = 'visa_transactions'
    # Create a faker object
    fake = Faker()
    # Generate card number and security code details
    card_security = createCard_SecurityCode(30, fake)
    # Create a DefaultDict to count the occurrences of same card
    customers = defaultdict(int)
    count = 0
    while True:
        # Derive Card Number
        cc_number = random.choice(list(card_security.keys()))
        customer = FakeCreditCardData(fake.credit_card_provider('visa'),
                                      cc_number,
                                      card_security[cc_number],
                                      fake.credit_card_expire
                                      (start='now', end='+10s', date_format="%m-%d-%y %H:%M:%S"))
        # Produce records to the topic
        producer.produce(topic, customer.json_serialization(), fake.credit_card_provider('visa'),
                         callback=delivery_callback)

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()
