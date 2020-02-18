import time
import Block
import User
import requests

class BlockChain:
    def __init__(self, ownerDetails):
        self.currentBlock = Block.Block(-1,[],-1,-1)
        self.ledger = [] # type: List[Block.Block]
        self.owerDetails = User.User(ownerDetails.userID, ownerDetails.name, ownerDetails.username, ownerDetails.mobile, ownerDetails.email, ownerDetails.address)
        self.nodesIP = []
        self.landDetails = {}
        self.pendingTransLog = []

    def clear(self):
        # every data member stored will be cleared
        self.currentBlock = Block.Block(-1,[],-1,-1)
        self.nodesIP = []
        self.landDetails = []
    # def init():

    def checkLedger(self, data):
        
        if(self.owerDetails.verify(data)):
            hash_pre = 0
            for block in self.ledger:
                if hash_pre != block.previous_hash:
                    return False
                hash_pre = block.compute_hash()
            return True
        else:
            return False

    def requestBuy(self, landID, offerPrice):
        URL = "http://localhost:3030/requestBuy"
        data = {'landID':landID, 'offer':offerPrice}
        res = requests.post(url = URL, data = data)
        print("Request to buy land : %d is sent. Response : %s",landID,res.text)
        return 

    def mine(self):
        if self.currentBlock.verify():
            while not self.currentBlock.mine():
                return True
        return False

    def getOfferList(self, landID):
        URL = "http://localhost:3030/offers"
        PARAMS = {'landID':landID}
        res = requests.get(url = URL, params = PARAMS)
        return res.json().list

    def acceptOffer(self, landID, offerID):
        URL = "http://localhost:3030/acceptOffer"
        PARAMS = {'landID':landID, 'offerID':offerID}
        res = requests.get(url = URL, params = PARAMS)

        if res.json().status == 'ok':
            return True
        else:
            return str(res.json().error)        
    
