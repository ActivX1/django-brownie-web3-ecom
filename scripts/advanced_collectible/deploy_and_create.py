from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
)
from brownie import AdvancedCollectible, network, config

def deploy_and_create():
    account = get_account()
    # We want to be able to use the deployed contracts if we are on a testnet
    # Otherwise, we want to deploy some mocks and use those
    # Rinkeby
    advanced_collectible = AdvancedCollectible.deploy({"from": account})
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("New token has been created!")
    return advanced_collectible, creating_tx


def main():
    deploy_and_create()