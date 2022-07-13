#!/usr/bin/env python

import random
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer
from collections import defaultdict
from card_transactions_helper import *

msg_partition = {}


# Read Default section of config file
def read_default_configuration(config_file: str) -> Producer:
    # Parse the configuration.
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    config_parser = ConfigParser()
    config_parser.read_file(args.config_file)
    config = dict(config_parser['default'])
    return config


# Optional per-message delivery callback (triggered by poll() or flush())
# when a message has been successfully delivered or permanently failed delivery (after retries).
def delivery_callback(err, msg):
    if err:
        print('ERROR: Message failed delivery: {}'.format(err))
    else:
        print("Produced event to topic {topic}, partition {partition}: key = {key:12} value = {value:12}".format(
            topic=msg.topic(), partition=msg.partition(), key=msg.key().decode('utf-8'),
            value=msg.value().decode('utf-8')))
        msg_partition[msg.key().decode('utf-8')] = msg.partition()


# Produce Messages
def produce_messages(producer_obj: Producer):
    # Topic to write messages
    topic = args.topic_name
    # Generate card number and security code details
    cc_details = generate_card_details(30)
    # Create a DefaultDict to count the occurrences of same card
    customers = defaultdict(int)
    count = 0
    while True:
        for _ in range(50):
            customer = generate_card_transaction(cc_details)
            # Produce records to the topic
            producer.produce(topic, customer.json_serialization(), customer.card_type,
                             callback=delivery_callback)

        producer.poll(args.poll_time)


if __name__ == '__main__':
    # Parse the command line.
    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'))          # Add argument for configuration file
    parser.add_argument('--topic_name', type=str, required=True)    # Add argument for topic name
    parser.add_argument('--poll_time', type=int, required=False, default=1)     # Add argument for producer poll time
    args = parser.parse_args()
    print(args.topic_name, args.poll_time)

    config_default = read_default_configuration(args.config_file)
    # Create Producer instance
    producer = Producer(config_default)
    print(config_default.items())

    # Produce messages to Kafka Topic
    produce_messages(producer)

    # Block until the messages are sent.
    # producer.poll(10000)
    # producer.flush()
