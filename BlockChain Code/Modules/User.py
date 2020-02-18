


class User:
    def __init__(self, id, name, username, mobile, email, address):
        self.userID = id
        self.name = name
        self.username = username
        self.mobile = mobile
        self.email = email
        self.address = address
    
    def verify(self, data):
        # get details userID details from main server
        if(data.userID==self.userID and data.name == self.name and data.username == self.username and data.mobile == self.mobile and data.email == self.email and data.address == self.address):
            return True
        else:
            return False
    
    
    def update(self, id, username, name, mobile, email, address):
        self.userID = id
        self.username = username
        self.name = name
        self.mobile = mobile
        self.email = email
        self.address = address
    
    # def checkSession(): 
    # may be built after sometime
