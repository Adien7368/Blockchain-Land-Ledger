

class Transaction:
    def __init__(self, price, landID, buyerID, documents, sellerDetails):
        self.price = price
        self.landID = landID
        self.buyerID = buyerID
        self.documents = documents
        self.sellerID = sellerDetails
    def verify():
        publicKey = 0 # getting seller public key from server
        #
        #   decrypt sellers digitalSign and check the
        #   signature
        #   we will ignore the documents check
        #   we can add a moderator digitalSign that can verify the
        #   documents
    
