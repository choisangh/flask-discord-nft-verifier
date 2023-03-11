from web3 import Web3
from eth_account.messages import encode_defunct


class Web3Manager:
    def __init__(self, config):
        self.WEB3_PROVIDER_URI = config.WEB3_PROVIDER_URI

    def verify_signature(self, message, signature, address):
        w3 = Web3(Web3.HTTPProvider(self.WEB3_PROVIDER_URI))
        message_hash = encode_defunct(text=message)
        signature_bytes = bytes.fromhex(signature[2:])
        signer = w3.eth.account.recover_message(message_hash, signature=signature_bytes)
        return signer.lower() == address.lower()

