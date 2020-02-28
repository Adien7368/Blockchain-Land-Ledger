
import requests

URLS = {
    'login':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/login_api/login.php',
    'walletID':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/wallet_api/read_single.php?wallet_id=',
    'wallet':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/wallet_api/read.php',
    'landID':'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/land_api/read_single.php?land_id=',
    'land' : 'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/land_api/read.php',
    'userID' : 'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/user_api/read_single.php?id=',
    'user' : 'http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/user_api/read.php'
}


PAGES = {
    'login':'login.html'
}


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
    print(data)
    try:
        return (data['message']=='success')
    except:
        return False

def userinfo(id):
    res = requests.get(url = URLS['userID']+str(id))
    data = res.json()
    print (data)
    return data