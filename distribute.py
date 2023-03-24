from web3 import Web3, HTTPProvider
import json

# 填写智能合约地址
CONTRACT_ADDRESS = "0x548Da0F6b0AFD0094F735503D44e79a3769980Fd"

# 填写节点的HTTP RPC地址
w3 = Web3(Web3.HTTPProvider("https://eth-goerli.g.alchemy.com/v2/L3VVGzT6kYXwWIUCf1nqxXUukjKlWHzc"))

def getbalance(address):
    balance = w3.fromWei(w3.eth.getBalance(address), "ether")
    print("当前账户的余额" + str(balance))

def main():
    address = '0x641FB7dd0DEC385cB369FC9F87F5C54eD33B01BF'
    getbalance(address)

if __name__ == "__main__":
    main()
