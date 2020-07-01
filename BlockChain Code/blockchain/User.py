
class User:
    def __init__(self):
        self.userID = -1
        self.name = ''
        self.username = ''
        self.mobile = -1
        self.email = ''
        self.address = ''
        self.walletID = -1
        self.login = False
        self.dob = ''


    
    def verify(self, data):
        # get details userID details from main server
        if(self.login == True and data.userID==self.userID and data.name == self.name and data.username == self.username and data.mobile == self.mobile and data.email == self.email and data.address == self.address):
            return True
        else:
            return False
    

    def update(self, data):
        self.userID = data['id']
        self.username = data['user_name']
        self.name = data['name']
        self.mobile = data['phone']
        self.email = data['email']
        self.address = data['address']
        self.dob = data['dob']

    def logintry(self, data):
        try:
            self.update(data)
        except:
            print ('\terror USER: <check your data>')
            return False
        self.login = True
        print('updated local object USER: ok')
        return True
    
    def logout(self):
        self.userID = -1
        self.name = ''
        self.username = ''
        self.mobile = -1
        self.email = ''
        self.address = ''
        self.login = False
    

    
    # def checkSession(): 
    # may be built after sometime
