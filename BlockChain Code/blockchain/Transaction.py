import nacl.encoding
import nacl.signing
import requests
import config.utils as cfg
import uuid
class Transaction:
    def __init__(self, price, landID, sellerID, buyerID, sellSign, buySign, documents):
        self.index = uuid.uuid4().hex
        self.price = price
        self.landID = landID
        self.sellerID = sellerID
        self.buyerID = buyerID
        self.sellSign = sellSign
        self.buySign = buySign
        self.documents = documents
    
    def signBuyer(self):
        pbuyKey = cfg.privateKey(self.buyerID)
        if (pbuyKey == ''):
            return False
        pbuyKey = nacl.signing.SigningKey(pbuyKey, encoder=nacl.encoding.HexEncoder)
        buySign = pbuyKey.sign(self.__str__().encode(), encoder=nacl.encoding.HexEncoder)
        self.buySign = buySign
        return True
        
    def signSeller(self):
        psellKey = cfg.privateKey(self.sellerID)
        if (psellKey == ''):
            return False
        psellKey = nacl.signing.SigningKey(pbuyKey, encoder=nacl.encoding.HexEncoder)
        sellSign = psellKey.sign(self.__str__(), encoder=nacl.encoding.HexEncoder)
        self.sellSign = sellSign
        return True
        
    def verifySignBuyer(self):
        try:
            buyKey = cfg.publicKey(self.buyerID)
            buyKey = nacl.signing.VerifyKey(buyKey, encoder=nacl.encoding.HexEncoder)
            buy = buyKey.verify(self.buySign)
            if(cfg.compareJSON(self, buy)):
                return True
            else:
                return False
        except nacl.exceptions.BadSignatureError:
            return False

    def verifySignSeller(self):
        try:
            sellKey = cfg.publicKey(self.sellerID)
            sellKey = nacl.signing.VerifyKey(sellKey, encoder=nacl.encoding.HexEncoder)
            sell = sellKey.verify(self.sellSign)
            if(cfg.compareJSON(self, buy)):
                return True
            else:
                return False
        except nacl.exceptions.BadSignatureError:
            return False

    def verify(self):
        # getting seller public key from server
        #
        #   decrypt sellers digitalSign and check the
        #   signature
        #   we will ignore the documents check
        #   we can add a moderator digitalSign that can verify the
        #   documents
        if (self.verifySignBuyer() and self.verifySignSeller()):
            return True
        else:
            return False
        



    
