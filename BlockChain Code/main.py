from flask import Flask, request, redirect, url_for, render_template 
from blockchain import BlockChain
import requests
import config.utils as cfg
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





if __name__ == '__main__':
    app.run(debug=True, port=cfg.PORT)


