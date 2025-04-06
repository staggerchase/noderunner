from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

block = w3.eth.get_block('latest')
print("Latest Block:")
print(f"Number: {block.number}")
print(f"Hash: {block.hash.hex()}")
print(f"Transactions: {len(block.transactions)}")
