<?php


class Database {
    // DB params
    private $host ='127.0.0.1';
    private $db_name='ledger';
    private $username = 'root';
    private $password=null;
    private $conn;

    //DB connect
    public function connect(){
        $this->conn=null;

        try{
            $this->conn=new PDO('mysql:host='.$this->host.';dbname='.$this->db_name,
                $this->username, $this->password);
            $this->conn->setAttribute(PDO::ATTR_ERRMODE,
                PDO::ERRMODE_EXCEPTION);
        } catch(PDOException $e){
            echo "connection error".$e->getMessage();
        }
        return $this->conn;

    }

}