# venv is virtual environment of python
## A server that will return the ip of blockchain member

API Documentation


## User
Return all details of users
[GET] [nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/user_api/read.php

Return details of user whose user name is user_name
[GET] [nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/user_api/read_user.php?user_name=?

Return details of user with user id = :id
[GET] [nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/user_api/read_single.php?id=?

## Register User
register a user in login and user table
[POST] [user_name = String, user_pass = String, name = String, email = String, wallet_id = Int, phone = Int, address = String, dob = String, dig_sign = String]
http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/login_api/register.php

## land
Return details of all lands 
[GET] [nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/land_api/read.php

Return a land details havinga given landID
[GET] [nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/land_api/read_single.php?land_id=?


## wallet
Return all details of wallets
[GET] [nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/wallet_api/read.php

Return all wallet details with a walletID
[GET] [nothing] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/wallet_api/read_single.php?wallet_id=?


## login
login meathod 
[POST] [user_name = String, user_pass = String] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/login_api/login.php


## ip 
Read all peer ip
[GET] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/ip_api/login.php

Register a peer
[POST] [id = Int,address = String] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/ip_api/create.php

delete a peer
[GET] [id = Int] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/ip_api/delete.php

## transaction request
create a request oof transaction
[POST] [price = Double, land_id = Int, seller_id = Int, buyer_id = Int, inspector_id = Int, buy_hex = String, sell_hex = String, inspector_hex = String, documents = String] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/request_trans_api/create.php

delete a particular request
[DELETE] [land_id = Int, seller_id = Int, buyer_id = Int] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/request_trans_api/delete.php

get request for a particular seller
[GET] [id = Int] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/request_trans_api/my_request.php?id=

to sign a request for INSPECTOR
[PUT] [land_id = Int, seller_id = Int, buyer_id = Int, inspector_hex = String] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/request_trans_api/inspector_sign.php

to sign a request for SELLER
[PUT] [land_id = Int, seller_id = Int, buyer_id = Int, sell_hex = String] http://13.127.187.57/project/Blockchain-Land-Ledger/Server/Rest-APIs-master/api/request_trans_api/seller_sign.php
