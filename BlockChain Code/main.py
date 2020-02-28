from flask import Flask, request, redirect, url_for, render_template 
from blockchain import BlockChain
import requests
import utils
app = Flask(__name__, template_folder='Pages')

blockC = BlockChain.BlockChain()




@app.route('/login', methods = ['GET'])
def login():
    return render_template(utils.PAGES['login'])


## Retry login page
@app.route('/login/<int:retry>', methods = ['GET'])
def loginretry(retry):
    print(retry)
    if(retry==1):
        return render_template(utils.PAGES['login'])
    else:
        return redirect(url_for("login"))



@app.route('/login', methods = ['POST'])
def loginCheck():
    # try:
    user = request.form['user_name']
    passw = request.form['user_pass']
    data = utils.userlogin(user, passw)
    if(data):
        res = blockC.login(user, passw, utils.userlogin, utils.userinfo, utils.landinfo)
        if(res):
            return 'To dashboard'
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
        redirect(url_for("login"))




if __name__ == '__main__':
    app.run(debug=True)


