import nacl.encoding
import nacl.signing
import requests
import config.utils as cfg

class Transaction:
    def __init__(self, index, price, landID, sellerID, buyerID, inspectID, sellSign, buySign, inspectSign, documents):
        self.index = index
        self.price = price
        self.landID = landID
        self.sellerID = sellerID
        self.buyerID = buyerID
        self.inspectID = inspectID
        self.sellSign = sellSign
        self.buySign = buySign
        self.inspectSign = inspectSign
        self.documents = documents
    
    # def signBuyer(self, buyerID):


    def verify(self):
        # getting seller public key from server
        #
        #   decrypt sellers digitalSign and check the
        #   signature
        #   we will ignore the documents check
        #   we can add a moderator digitalSign that can verify the
        #   documents
        try:
            sellKey = cfg.publicKey(self.sellerID)
            buyKey = cfg.publicKey(self.buyerID)
            inspectKey = cfg.publicKey(self.inspectID)

            sellKey = nacl.signing.VerifyKey(sellKey, encoder=nacl.encoding.HexEncoder)
            buyKey = nacl.signing.VerifyKey(buyKey, encoder=nacl.encoding.HexEncoder)
            inspectKey = nacl.signing.VerifyKey(inspectKey, encoder=nacl.encoding.HexEncoder)

            buy = buyKey.verify(self.buySign)
            sell = sellKey.verify(self.sellSign)
            inspect = inspectKey.verify(self.inspectSign)
            if(cfg.compareJSON(self, buy) and cfg.compareJSON(self, sell) and cfg.compareJSON(self, inspect)):
                return True
            else:
                return False
        except nacl.exceptions.BadSignatureError:
            return False
        



    
