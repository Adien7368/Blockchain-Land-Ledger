
import requests
import json
import socket
import blockchain.Transaction


URLS = {
    'login':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/login_api/login.php',
    'walletID':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/wallet_api/read_single.php?wallet_id=',
    'wallet':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/wallet_api/read.php',
    'landID':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/land_api/read_single.php?land_id=',
    'land' : 'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/land_api/read.php',
    'userID' : 'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/user_api/read_single.php?id=',
    'user' : 'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/user_api/read.php',
    'userName':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/user_api/read_user.php?user_name=',
    'userCreate': 'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/login_api/register.php',
    'ipRead':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/ip_api/login.php',
    'ipRegis':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/ip_api/create.php',
    'ipDelete':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/ip_api/delete.php'
}


PAGES = {
    'login':'Login/index.html',
    'logintry':'Login/retryindex.html',
    'regisUser':'Register/index.html',
    'intro':'Intro/index.html',
    'dashboard':'Dashboard/index.html'
}


def ipRead():
    res = requests.get(url = URLS['ipRead'])
    data = res.json()
    return data

def ipUser(id):
    res = requests.get(url = URLS['ipUser'], json={"userID":id})
    data = res.json()
    print("address :" + str(data))
    return data

def ipRegis(userID, address):
    res = requests.post(url = URLS['ipRegis'], json={"id":userID, "address":address})
    data = res.json()
    print("Register ip : " + str(data))
    return data

def ipDelete(userID):
    res = requests.post(url = URLS['ipDelete'], json={"id":userID})
    data = res.json()
    print("Delete ip : "+str(data))
    return data

def landinfoAll():
    res = requests.get(url = URLS['land'])
    data = res.json()
    print(data)
    return data

def landinfo(id):
    res = requests.get(url = URLS['landID']+str(id))
    data = res.json()
    print(data)
    return data

def userinfoAll():
    res = requests.get(url = URLS['user'])
    data = res.json()
    print (data)
    return data

def userlogin(user, passw):
    res = requests.post(url = URLS['login'], json = {"user_name":user,"user_pass":passw})
    data = res.json()
    print("Login : "+str(data))
    try:
        return (data['message']=='success')
    except:
        return False

def userinfo(id):
    res = requests.get(url = URLS['userID']+str(id))
    data = res.json()
    print ("UserID Info : "+str(data))
    return data

def usernameinfo(username):
    res = requests.get(url = URLS['userName']+str(username))
    data = res.json()
    print("Username Info : "+ str(data))
    return data


def publicKey(userID):
    obj = userinfo(userID)
    Key = json.loads(obj['dig_sign'])
    return Key['pub']
    
def compareJSON(obj, jsonStr):
    objc = json.loads(jsonStr)
    for key in objc:
        if( not (key in obj and objc[key] == obj[key])):
            return False
    return True

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def parseTransaction(obj):
    return blockchain.Transaction.Transaction(obj['index'],obj['price'],obj['landID'],obj['sellerID'],obj['buyerID'],obj['inspectID'],obj['sellSign'],obj['buySign'],obj['inspectSign'],obj['documents'])
