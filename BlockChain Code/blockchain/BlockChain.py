import time
import requests
from blockchain import Block
from blockchain import User
import config.utils as cfg
import time
import json

class BlockChain:
    def __init__(self):
        self.port = 5000
        self.ledger = [Block.Block(0,[],0,0)] # type: List[Block.Block]
        self.ownerDetails = User.User()
        self.nodesIP = []
        self.landDetails = {}
        self.transactionIndex = {} # store all transactions on the blockChain
        self.transPool={}    # approved checked block waiting to be mined

    def addIP(self, id, address):
        self.nodesIP.append((id, address))

    def islogin(self):
        return self.ownerDetails.login

    def insertTransaction(self, obj):
        self.transPool[obj.index] = obj
        
    def distribute(self, obj, path):
        for peer in self.nodesIP:
            res = requests.post(peer['address']+path, json=obj)
            print("Sending trans.. "+peer['address']+":"+str(res))
    
    # def upadatePeers(self, peers):
    #     self.nodesIP = peers
    
    def login(self, user, passw):
        print(self.port)
        if(cfg.userlogin(user, passw)):
            data = cfg.usernameinfo(user)
            if('message' in data and data['message']=='success'):
                check = self.ownerDetails.logintry(data)
                if check:
                    self.landDetails = cfg.landinfo(self.ownerDetails.userID)    
                    cfg.ipRegis(self.ownerDetails.userID, str(cfg.getIP())+":"+str(self.port))
                    self.nodesIP = cfg.ipRead()
                    print ("NodeIP: ")
                    print(self.nodesIP)
                    data = {'id':self.ownerDetails.userID,'address':cfg.getIP()+":"+str(self.port)}
                    #self.distribute(data, '/imhere')
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
        if(len(self.transPool)==0):
            return False
        blo = Block.Block(len(self.ledger), self.transPool, time.time(), self.ledger[-1].compute_hash())
        if (not blo.mine()):
            return False
        for tran in self.transPool:
            self.transactionIndex[tran] = self.transPool[tran]
        self.transPool = {}
        self.ledger.append(blo)
        data = {'userID':self.ownerDetails.userID, 'ledger':self.ledger}
        self.distribute(data, '/register/blockchain')
        return True

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
    
