from hashlib import sha256
import json
import random
from blockchain import Transaction
LIMIT = 100000

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
    
    def update(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash

    def mine(self):
        for x in range(100000):
            self.nouce = random.randint(1,10000000)
            if self.compute_hash()< sha256(str(LIMIT).encode()).hexdigest():
                return True
        return False
    
    def verify(self):
        for t in self.transactions:
            if not self.transactions[t].verify():
                return False
        return True 

    def insert(self, transac):
        self.transactions.append(transac)
        