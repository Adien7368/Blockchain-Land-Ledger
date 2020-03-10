from flask import Flask, request, redirect, url_for, render_template 
from blockchain import BlockChain
import requests
import config.utils as cfg
import json
import nacl.signing
import nacl.encoding

app = Flask(__name__, template_folder='Pages')

blockC = BlockChain.BlockChain()




@app.route('/login', methods = ['GET'])
def login():
    if(blockC.islogin()):
        return redirect(url_for("dashboard"))
    return render_template(cfg.PAGES['login'])


## Retry login page
@app.route('/login/<int:retry>', methods = ['GET'])
def loginretry(retry):
    if(blockC.islogin()):
        return redirect(url_for("dashboard"))
    if(retry==1):
        return render_template(cfg.PAGES['login'])
    else:
        return redirect(url_for("login"))



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
    return redirect(url_for("loginretry",retry=1))
    # except:
    #     print("Some Error Occured")
    #     return redirect(url_for("login"))


@app.route('/dashboard', methods = ['GET'])
def dashboard():
    if(blockC.islogin()):
        return ''
    else:
        return redirect(url_for("login"))

@app.route('/logout', methods = ['GET'])
def logout():
    if(not blockC.islogin()):
        return redirect(url_for("login"))
    print("logout : " + str(blockC.logout()))
    return redirect(url_for("login"))


@app.route('/imhere', methods=['POST'])
def pingIP():
    try:
        obj = json.loads(request.get_data())
        blockC.addIP(obj['id'],obj['address'])
        return "Hello : "+obj['id']
    except:
        return "Wrong IP format"


@app.route('/register/user', methods=['GET'])
def registerUserUI():
    return render_template(cfg.PAGES['regisUser'])

@app.route('/register/user', methods=['POST'])
def registerUser():
    try:
        user = {}
        user['user_name'] = request.form['user_name']
        user['user_pass'] = request.form['user_pass']
        user['name'] = request.form['name']
        user['email'] = request.form['email']
        user['phone'] = request.form['phone']
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
            return redirect(url_for("registerUser"))
    except:
        return redirect(url_for("registerUser"))

@app.route('/register/transaction', methods=['POST'])
def regTransaction():
    obj = json.loads(request.get_data())
    try:
        tran = cfg.parseTransaction(obj)
        if(tran.index in blockC.transactionIndex):
            raise "Transaction Already Reached"
        if(tran.verify()):
            blockC.insertTransaction(tran)
            blockC.distribute(obj)
            return "Thanks for sharing"
        else:
            raise "Transaction is wrong"
    except:
        return 'Bye'




if __name__ == '__main__':
    app.run(debug=True, port=cfg.PORT)


