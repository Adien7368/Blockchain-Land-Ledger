# venv is virtual environment of python
## A server that will return the ip of blockchain member

API Documentation


##User
http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/user_api/read.php
#returns all user details of all users 

http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/user_api/read_single.php?id=?
#returns all user details of selected user, put id in place of ?


##land
http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/land_api/read.php
#returns all land details of all lands 

http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/land_api/read_single.php?land_id=?
#returns all land details of selected land, put id in place of ?


##wallet
http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/wallet_api/read.php
#returns all wallet details of all wallets 

http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/wallet_api/read_single.php?wallet_id=?
#returns all wallet details of selected wallet, put id in place of ?



##login
http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/login_api/login.php
send user_name and user_pass in json format, use post method
example- {"user_name"="paw","user_pass"="123"}

it will return 'successs' if user_name and user_pass are correct, 'user doesn't exist' if user not exists, and 'failed' otherwise


##register





