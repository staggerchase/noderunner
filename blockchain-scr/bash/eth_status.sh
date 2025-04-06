#!/bin/bash
NODE_URL="http://localhost:8545"
curl -s -X POST --data '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}' \
     -H "Content-Type: application/json" $NODE_URL
