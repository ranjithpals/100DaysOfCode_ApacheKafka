#!/usr/bin/env python

import sys
from random import choice
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer

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

    # Produce data by selecting random values from these lists.
    topic = "cc_transactions"
    cc_numbers = ['34643', '12567', '69869', '99989', '66667']
    transaction_ts = ['2022-04-01 10:30:45.333', '2022-04-01 10:30:46.222', '2022-04-01 10:30:47.501']
    card_type = 'visa'

    count = 0
    for _ in range(50):

        cc_num = choice(cc_numbers)
        trans_ts = choice(transaction_ts)
        msg = "{\"cc_num\":"+cc_num+",\"trans_ts\":"+trans_ts+"\"}"
        producer.produce(topic, msg, card_type, callback=delivery_callback)
        count += 1

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()