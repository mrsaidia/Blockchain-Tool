from web3 import Web3
from eth_account import Account
import csv
Account.enable_unaudited_hdwallet_features()
def getWalletInfos(mnemonic):
    acct = Account.from_mnemonic(
        mnemonic
    )
    fieldnames = ['phrase', 'address','private_key']
    rows = [
        {   
            'phrase':mnemonic,
            'address':acct.address,
            'private_key':acct.key.hex(),

        }
    ]

    with open('WalletFromPhrase.csv', 'a', encoding='UTF8', newline='') as f1:
        writer = csv.DictWriter(f1, fieldnames=fieldnames)
        writer.writerows(rows)

file_path = "list_phrase.txt"
with open(file_path, "r+", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

for line in lines:
    getWalletInfos(line)


