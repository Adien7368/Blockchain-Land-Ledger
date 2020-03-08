# venv is virtual environment of python
## A server that will return the ip of blockchain member

API Documentation


##User
Return all details of users
[GET][nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/user_api/read.php

Return details of user whose user name is user_name
[GET][nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/user_api/read_user.php?user_name=?

Return details of user with user id = :id
[GET][nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/user_api/read_single.php?id=?

##Register User
register a user in login and user table
[POST][user_name = string, user_pass = string, name = string, email = string, wallet_id = int, phone = int, address = string, dob = string, dig_sign = string]
http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/login_api/register.php

##land
Return details of all lands 
[GET][nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/land_api/read.php

Return a land details havinga given landID
[GET][nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/land_api/read_single.php?land_id=?


##wallet
Return all details of wallets
[GET][nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/wallet_api/read.php

Return all wallet details with a walletID
[GET][nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/wallet_api/read_single.php?wallet_id=?


##login
login meathod 
[POST][user_name = string, user_pass = string]http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/login_api/login.php


## ip 
Read all peer ip
[GET] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/ip_api/login.php

Register a peer
[POST][id = int,address = string] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/ip_api/create.php

delete a peer
[GET][id = int] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/ip_api/delete.php

