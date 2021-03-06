from eth_connector import EthConnector, EthConfig


class Verificator:

    def __init__(self, config: EthConfig):
        self.eth_connector = EthConnector(config)

    def verify_masternode(self, pub_key: str, message: str) -> bool:
        # TODO: Implement
        # 1. Read masternode pub key from blockchain and compare with provided
        # 2. Decrypt message with masternode pubkey
        return True

    def verify_neurocontract(self, contract_addr: str) -> bool:
        # TODO: Implement
        # 1. Create contract instance
        # 2. Verify prepaid balance?
        return True
