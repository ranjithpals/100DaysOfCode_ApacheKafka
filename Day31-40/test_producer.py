
import card_transactions_helper as cc_for_test

if __name__ == "__main__":
    cc_details = cc_for_test.generate_card_details(10)
    for k, v in cc_details.items():
        print(f'Card Number:{k}, \t {v}')
    transaction = cc_for_test.generate_card_transaction(cc_details)
    print("Sample Transaction")
    print(transaction)