from flask import Flask, request, redirect, url_for, render_template ,send_from_directory, send_file
from blockchain import BlockChain
import requests
import config.utils as cfg
import json
import nacl.signing
import nacl.encoding
import argparse
import time
parser = argparse.ArgumentParser()
parser.add_argument('-p', help='port number')
args = parser.parse_args()
port = 5000

if(args.p):
    port = args.p
# setting the template directory to /Pages
app = Flask(__name__, template_folder='Pages')

#serving files 
@app.route('/temp/<path:path>')
def forDebugging(path):
    return send_from_directory('Pages/map', path)

@app.route('/dashboard/<path:path>')
def sendDashFiles(path):
    return send_from_directory('Pages/Dashboard', path)

@app.route('/intro/<path:path>')
def sendIntroFiles(path):
    # print(path)
    return send_from_directory('Pages/Intro', path)

@app.route('/login/<path:path>')
def sendFiles(path):
    # print(path)
    return send_from_directory('Pages/Login', path)

@app.route('/register/<path:path>')
def sendRegisFiles(path):
    return send_from_directory('Pages/Register', path)

#user regis page
@app.route('/regisUser', methods = ['GET'])
def regisUser():
    return render_template(cfg.PAGES['regisUser'])

#intro page
@app.route('/', methods = ['GET'])
def hello():
    return render_template(cfg.PAGES['intro'])

# creating global blockchain 
blockC = BlockChain.BlockChain()
blockC.port = port

@app.route('/login', methods = ['GET'])
def login():
    if(blockC.islogin()):
        return redirect(url_for("dashboard"))
    return render_template(cfg.PAGES['login'])


## Retry login page
@app.route('/logintry', methods = ['GET'])
def loginretry():
    if(blockC.islogin()):
        return redirect(url_for("dashboard"))
    return render_template(cfg.PAGES['login'])



@app.route('/login', methods = ['POST'])
def loginCheck():
    # try:
    # if(blockC.islogin()) return redirect(url_for("dashboard"))
    user = request.form['user_name']
    passw = request.form['user_pass']
    res = blockC.login(user, passw)
    if(res):
        return redirect(url_for("dashboard"))
    print (url_for("loginretry", retry=1))
    return redirect(url_for("loginretry"))
    # except:
    #     print("Some Error Occured")
    #     return redirect(url_for("login"))

@app.route('/map', methods = ['GET'])
def mapstart():
    return render_template(cfg.PAGES['map'])

@app.route('/notifications', methods = ['GET'])
def notifications():
    return render_template(cfg.PAGES['notification'])

@app.route('/requests', methods = ['GET'])
def requ():
    return render_template(cfg.PAGES['requests'])

@app.route('/tables', methods = ['GET'])
def tab():
    return render_template(cfg.PAGES['table'])

@app.route('/user', methods = ['GET'])
def userprofile():
    if(blockC.islogin()):
        return render_template(cfg.PAGES['user'] ,
            name = blockC.ownerDetails.name, 
            username = blockC.ownerDetails.username, 
            email = blockC.ownerDetails.email,
            address = blockC.ownerDetails.address,
            dob = blockC.ownerDetails.dob)
    else:  
        return render_template(cfg.PAGES['login'])

@app.route('/dashboard', methods = ['GET'])
def dashboard():
    if(blockC.islogin()):
        return render_template(cfg.PAGES['user'] ,
            name = blockC.ownerDetails.name, 
            username = blockC.ownerDetails.username, 
            email = blockC.ownerDetails.email,
            address = blockC.ownerDetails.address,
            dob = blockC.ownerDetails.dob)
    else:
        return redirect(url_for("login"))
    
@app.route('/logout', methods = ['GET'])
def logout():
    if(not blockC.islogin()):
        return redirect(url_for("login"))
    print("logout : " + str(blockC.logout()))
    return redirect(url_for("login"))

# not 
@app.route('/imhere', methods=['POST'])
def pingIP():
    try:
        obj = json.loads(request.get_data())
        blockC.addIP(obj['id'],obj['address'])
        return "Hello : "+obj['id']
    except:
        return "Wrong IP format"


@app.route('/regisUser', methods=['GET'])
def registerUserUI():
    return render_template(cfg.PAGES['regisUser'])

@app.route('/register/user', methods=['POST'])
def registerUser():
    try:
        user = {}
        print(request.form)
        user['user_name'] = request.form['user_name']
        user['user_pass'] = request.form['user_pass']
        user['name'] = request.form['name']
        user['email'] = request.form['email']
        user['phone'] = request.form['phone'].replace('-','')
        user['address'] = request.form['address']
        user['dob'] = request.form['dob']
        prikey = nacl.signing.SigningKey.generate()
        pubkey = prikey.verify_key
        dig_sign = {'pub':pubkey.encode(nacl.encoding.HexEncoder),'pri':prikey.encode(nacl.encoding.HexEncoder)}
        user['dig_sign'] = str(dig_sign)
        res = requests.post(cfg.URLS['userCreate'], json=user)
        data = res.json()
        print("User register response: "+str(data))
        if('message' in data and data['message']=='success'):
            return redirect(url_for("login"))
        else:
            return redirect(url_for("registerUserUI"))
    except:
        return redirect(url_for("registerUserUI"))

@app.route('/register/transaction', methods=['POST'])
def regTransaction():
    obj = json.loads(request.get_data())
    try:
        tran = cfg.parseTransaction(obj)
        if(tran.index in blockC.transactionIndex):
            raise "Transaction Already Reached"
        if(tran.verify()):
            blockC.insertTransaction(tran)
            blockC.distribute(obj,'/register/transaction')
            return "Thanks for sharing"
        else:
            raise "Transaction is wrong"
    except:
        return 'Bye'

@app.route('/register/blockchain', methods=['POST'])
def regBlockChain():
    obj = json.loads(request.get_data())
    try:
        userID, leg = cfg.parseLedger(obj)
    except:
        return 'Error'
    
    if(len(blockC.ledger)<len(leg)):
        blockC.ledger = leg
        tempTransIndex = {}
        for block in leg:
            for trans in block.transactions:
                tempTransIndex[trans.index] = trans
                if (not (trans.index in blockC.transactionIndex)):
                    blockC.transactionIndex[trans.index] = trans
                if (trans.index in blockC.transPool):
                    blockC.transPool.pop(trans.index)
                
    else:
        try:
            addr = cfg.ipUser(userID)
            data = {'userID':userID, 'ledger':blockC.ledger}
            res = requests.post(addr+"/register/blockchain", json = data)
        except:
            return 'Error happen'

@app.route('/mine', methods=['GET'])
def mine():
    if (not blockC.mine()):
        return 'Mine TLE'
    return "Block Added"



if __name__ == '__main__':
    app.run(debug=True, port=port)


