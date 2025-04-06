const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

async function readBalance(address) {
    const balance = await web3.eth.getBalance(address);
    console.log(`Balance of ${address}: ${web3.utils.fromWei(balance, 'ether')} ETH`);
}

readBalance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e');
