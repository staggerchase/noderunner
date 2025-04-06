const Web3 = require('web3');
const web3 = new Web3('https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID');

const senderPrivateKey = '0xYOUR_PRIVATE_KEY';
const senderAddress = '0xYOUR_ADDRESS';
const recipient = '0xRECIPIENT_ADDRESS';

async function send() {
    const tx = {
        to: recipient,
        value: web3.utils.toWei('0.01', 'ether'),
        gas: 21000
    };

    const signedTx = await web3.eth.accounts.signTransaction(tx, senderPrivateKey);
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log(receipt);
}

send();
