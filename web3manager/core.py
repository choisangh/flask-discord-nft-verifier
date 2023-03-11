from web3 import Web3
from eth_account.messages import encode_defunct
from web3.middleware import geth_poa_middleware


class Web3Manager:
    def __init__(self, config):
        self.w3 = Web3(Web3.HTTPProvider(config.WEB3_PROVIDER_URI))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.contract = self.w3.eth.contract(address=config.CONTRACT_ADDRESS, abi=config.ABI)

    def verify_signature(self, message, signature, address):

        message_hash = encode_defunct(text=message)
        signature_bytes = bytes.fromhex(signature[2:])
        signer = self.w3.eth.account.recover_message(message_hash, signature=signature_bytes)
        return signer.lower() == address.lower()

    def check_holder(self, address):
        balance = self.contract.functions.balanceOf(address).call()
        return balance > 0
