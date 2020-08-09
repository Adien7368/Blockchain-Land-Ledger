
import requests
import json
import ast
import socket
from blockchain import Transaction,Block


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
    'ipDelete':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/ip_api/delete.php',
    'createTransactionRequest':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/request_trans_api/create.php',
    'deleteTransactionRequest':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/request_trans_api/delete.php',
    'getRequestByID':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/request_trans_api/my_request.php?id='
}


PAGES = {
    'login':'Login/index.html',
    'logintry':'Login/retryindex.html',
    'regisUser':'Register/index.html',
    'intro':'Intro/index.html',
    'user':'Dashboard/user.html',
    'map':'Dashboard/map.html',
    'notification':'Dashboard/notifications.html',
    'table':'Dashboard/tables.html',
    'requests':'Dashboard/requests.html'
}

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def printErr(obj):
    print(colored(255,0,0,obj))

def printAPIData(obj):
    print(colored(0,255,0,obj))

def printLogData(obj):
    print(colored(255,255,0,obj))


def ipRead():
    res = requests.get(url = URLS['ipRead'])
    data = res.json()
    return data

def ipUser(id):
    res = requests.get(url = URLS['ipUser'], json={"userID":id})
    data = res.json()
    printAPIData("address :" + str(data))
    return data

def ipRegis(userID, address):
    res = requests.post(url = URLS['ipRegis'], json={"id":userID, "address":address})
    data = res.json()
    printAPIData("Register ip : " + str(data))
    return data

def ipDelete(userID):
    res = requests.post(url = URLS['ipDelete'], json={"id":userID})
    data = res.json()
    printAPIData("Delete ip : "+str(data))
    return data

def landinfoAll():
    res = requests.get(url = URLS['land'])
    data = res.json()
    printAPIData(data)
    return data

def landinfo(id):
    res = requests.get(url = URLS['landID']+str(id))
    data = res.json()
    printAPIData(data)
    return data

def userinfoAll():
    res = requests.get(url = URLS['user'])
    data = res.json()
    printAPIData(data)
    return data

def userlogin(user, passw):
    res = requests.post(url = URLS['login'], json = {"user_name":user,"user_pass":passw})
    data = res.json()
    printAPIData("Login : "+str(data))
    try:
        return (data['message']=='success')
    except:
        return False

def userinfo(id):
    res = requests.get(url = URLS['userID']+str(id))
    data = res.json()
    printAPIData("UserID Info : "+str(data))
    return data

def usernameinfo(username):
    res = requests.get(url = URLS['userName']+str(username))
    data = res.json()
    printAPIData("Username Info : "+ str(data))
    return data


def publicKey(userID):
    obj = userinfo(userID)
    Key = ast.literal_eval(obj['dig_sign'])
    return Key['pub']

def privateKey(userID):
    obj = userinfo(userID)
    Key = ast.literal_eval(obj['dig_sign'])
    return Key['pri']
    
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

def sendBuyRequest(data):
    # print ({'price':data.price,'land_id':data.landID,'seller_id':data.sellerID,'buyer_id':data.buyerID,'buy_hex':data.buySign.__str__(),'sell_hex':data.sellSign.__str__(),'documents':data.documents})
    res = requests.post(url = URLS['createTransactionRequest'], json={'price':data.price,'land_id':data.landID,'seller_id':data.sellerID,'buyer_id':data.buyerID,'buy_hex':data.buySign.__str__(),'sell_hex':data.sellSign.__str__(),'documents':data.documents})
    printAPIData(res)
    return True

# need update
def parseTransaction(obj):
    return Transaction.Transaction(obj['index'],obj['price'],obj['landID'],obj['sellerID'],obj['buyerID'],obj['sellSign'],obj['buySign'],obj['documents'])

def parseBlock(obj):
    return Block.Block(obj['index'],parseTransaction(obj['transaction']),obj['timestamp'],obj['previous_hash'],obj['nonce'])


def getNotification(seller_id):
    res = requests.get(url = URLS['getRequestByID']+str(seller_id))
    printAPIData(res.json())
    return res.json()
    
