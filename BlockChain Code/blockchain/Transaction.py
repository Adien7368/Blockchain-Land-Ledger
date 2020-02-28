import nacl.encoding
import nacl.signing
import requests

class Transaction:
    def __init__(self, price, landID, buyerID, documents, sellerDetails):
        self.price = price
        self.landID = landID
        self.buyerID = buyerID
        self.documents = documents
        self.sellerDetails = sellerDetails
        
    def verify(self):
        URL = "http://localhost:3030/pubkey"
        PARAMS = {'userID':self.sellerDetails.userID}  ##########
        data = requests.get(url = URL, params = PARAMS) ##########
        publicKey = data.json().publicKey     #################
        key =  nacl.signing.VerifyKey(publicKey, encoder = nacl.encoding.HexEncoder)
        # getting seller public key from server
        #
        #   decrypt sellers digitalSign and check the
        #   signature
        #   we will ignore the documents check
        #   we can add a moderator digitalSign that can verify the
        #   documents
        try:
            key.verify(self.sellerDetails.signed)
        except nacl.exceptions.BadSignatureError:
            return False
        return True



    
