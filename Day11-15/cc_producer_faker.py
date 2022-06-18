#!/usr/bin/env python

import sys
from random import choice
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer
from faker import Faker

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

    # Produce data by selecting random values from Faker library.
    fake = Faker()
    
    topic = 'cc_transactions'
    card_type = 'visa'
    
    while True:
        cc_num = fake.credit_card_number()
        trans_ts = fake.date_time()
        # print(cc_num, trans_ts) 
        msg = "{\"cc_num\":"+cc_num+",\"trans_ts\":"+str(trans_ts)+"}"
        producer.produce(topic, msg, card_type, callback=delivery_callback)
        #count += 1

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()