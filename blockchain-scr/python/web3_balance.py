from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

address = '0x742d35Cc6634C0532925a3b844Bc454e4438f44e'
balance = w3.eth.get_balance(address)
print(f'Balance: {w3.fromWei(balance, "ether")} ETH')
