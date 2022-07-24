from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
)
from brownie import AdvancedCollectible, network, config, Sales

def deploy_payments():
    account = get_account()
    # We want to be able to use the deployed contracts if we are on a testnet
    # Otherwise, we want to deploy some mocks and use those
    # Rinkeby
    payments = Sales.deploy({"from": account})
    creating_tx = payments.createCollectible({"from": account})
    creating_tx.wait(1)
    print("New token has been created!")
    return payments, creating_tx


def main():
    deploy_payments()