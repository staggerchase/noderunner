from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

account = w3.eth.account.from_key('0xYOUR_PRIVATE_KEY')
nonce = w3.eth.get_transaction_count(account.address)

tx = {
    'to': '0xRECIPIENT_ADDRESS',
    'value': w3.to_wei(0.01, 'ether'),
    'gas': 21000,
    'gasPrice': w3.to_wei('20', 'gwei'),
    'nonce': nonce,
    'chainId': 5  # Goerli Testnet
}

signed_tx = w3.eth.account.sign_transaction(tx, account.key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
print("Transaction sent:", w3.to_hex(tx_hash))
