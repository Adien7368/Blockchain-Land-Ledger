import time
import requests
from blockchain import Block
from blockchain import User
import config.utils as cfg
import time

class BlockChain:
    def __init__(self):
        self.currentBlock = Block.Block(-1,[],-1,-1)
        self.ledger = [Block.Block(0,[],0,0)] # type: List[Block.Block]
        self.ownerDetails = User.User()
        self.nodesIP = []
        self.landDetails = {}
        self.transactionIndex = {}
        self.transPool=[]

    def islogin(self):
        return self.ownerDetails.login

    def insertTransaction(self, obj):
        self.transPool.append(obj)
        
    def distribute(self, obj):
        for peer in self.nodesIP:
            res = requests.post(peer['address']+":"+cfg.PORT+"/register/new", json=obj)
            print("Sending trans.. "+peer['address']+":"+str(res))
    
    # def upadatePeers(self, peers):
    #     self.nodesIP = peers
    
    def login(self, user, passw):
        if(cfg.userlogin(user, passw)):
            data = cfg.userinfo(1)
            if('message' in data and data['message']=='success'):
                check = self.ownerDetails.logintry(data)
                if check:
                    self.landDetails = cfg.landinfo(self.ownerDetails.userID)    
                    cfg.ipRegis(self.ownerDetails.userID, cfg.getIP())
                    self.nodesIP = cfg.ipRead()
                    return True
        return False
    
    def logout(self):
        cfg.ipDelete(self.ownerDetails.userID)
        self.ownerDetails.logout()
        return 'done'

    def clear(self):
        # every data member stored will be cleared
        self.currentBlock = Block.Block(-1,[],-1,-1)
        self.nodesIP = []
        self.landDetails = []

    def checkLedger(self, data):
        if(self.ownerDetails.verify(data)):
            hash_pre = 0
            for block in self.ledger:
                if hash_pre != block.previous_hash:
                    return False
                hash_pre = block.compute_hash()
            return True
        else:
            return False

    # def requestBuy(self, landID, offerPrice):
    #     URL = "http://localhost:3030/requestBuy"
    #     data = {'landID':landID, 'offer':offerPrice}
    #     res = requests.post(url = URL, data = data)
    #     print("Request to buy land : %d is sent. Response : %s",landID,res.text)
    #     return 

    def mine(self):
        if self.currentBlock.verify():
            while not self.currentBlock.mine():
                return True
        return False

    # def getOfferList(self, landID):
    #     URL = "http://localhost:3030/offers"
    #     PARAMS = {'landID':landID}
    #     res = requests.get(url = URL, params = PARAMS)
    #     return res.json().list

    # def acceptOffer(self, landID, offerID):
    #     URL = "http://localhost:3030/acceptOffer"
    #     PARAMS = {'landID':landID, 'offerID':offerID}
    #     res = requests.get(url = URL, params = PARAMS)

    #     if res.json().status == 'ok':
    #         return True
    #     else:
    #         return str(res.json().error)        
    
