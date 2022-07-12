
import cc_helper_w_partition_key as cc_for_test

if __name__ == "__main__":
    cc_details = cc_for_test.generate_card_details(50, 6)
    for k, v in cc_details.items():
        print(f'Card Number:{k}, \t {v}')
    print(cc_for_test.card_provider_dict)
    transaction = cc_for_test.generate_card_transaction(cc_details)
    print("Sample Message to Kafka")
    print(f'Key: {transaction.card_type}, Message: {transaction.json_serialization()}')