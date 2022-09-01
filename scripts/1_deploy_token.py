from brownie import MmdToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def main():
    account = get_account()
    mmd_token = MmdToken.deploy(initial_supply, {"from": account})
    print(mmd_token.name())