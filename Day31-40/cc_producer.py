#!/usr/bin/env python

import random
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer
from collections import defaultdict
from card_transactions_helper import *


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
    print(config.items())

    '''
    Optional per-message delivery callback (triggered by poll() or flush())
    when a message has been successfully delivered or permanently failed delivery (after retries).
    '''
    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

    # Topic to write messages
    topic = 'credcard02'
    # Generate card number and security code details
    cc_details = generate_card_details(30)
    # Create a DefaultDict to count the occurrences of same card
    customers = defaultdict(int)
    count = 0
    while True:
        for _ in range(50):
            customer = generate_card_transaction(cc_details)
            # Produce records to the topic
            producer.produce(topic, customer.json_serialization(), customer.card_type(),
                             callback=delivery_callback)

        producer.poll(1)

    # Block until the messages are sent.
    # producer.poll(10000)
    # producer.flush()
