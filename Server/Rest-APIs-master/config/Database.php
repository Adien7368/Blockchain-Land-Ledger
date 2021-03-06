<?php


class Database {
    // DB params
    private $host ='hat';
    private $db_name='ledger';
    private $username = 'hat';
    private $password='hat';
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
