<?php

     class Post {
        private $conn;
        private $table='user';

        public $id;
        public $name;
        public $user_name;
        public $address;
        public $dob;
        public $phone;
        public $dig_sign;
        public $email;
        public $wallet_id;

        public function __construct($db)
        {
            $this->conn=$db;
        }

        public function read(){
            $query='SELECT * FROM user';
            $stmt=$this->conn->prepare($query);
            $stmt->execute();
            return $stmt;
        }

        public function read_single() {
            $query='SELECT * FROM user where id=:id limit 1';
            $stmt=$this->conn->prepare($query);
            $stmt->bindParam('id', $this->id);
            $stmt->execute();
            return $stmt;
        }

        public function read_user() {
            $query='SELECT * FROM user where user_name=:user_name limit 1';
            $stmt=$this->conn->prepare($query);
            $stmt->bindParam('user_name', $this->user_name);
            $stmt->execute();
            return $stmt;   
        }

        // create post

        public function create() {
            $query='INSERT INTO '.$this->table.' SET id=:id, user_name=:user_name, name=:name, email=:email, wallet_id=:wallet_id, phone=:phone, address=:address, dob=:dob, dig_sign=:dig_sign';
	    $stmt=$this->conn->prepare($query);
            $stmt->bindParam(':id', $this->id);
            $stmt->bindParam(':name', $this->name);
            $stmt->bindParam(':user_name', $this->user_name);
            $stmt->bindParam(':email', $this->email);
	    $stmt->bindParam(':wallet_id',$this->wallet_id);
	    $stmt->bindParam(':phone',$this->phone);
	    $stmt->bindParam(':address',$this->address);
	    $stmt->bindParam(':dob',$this->dob);
	    $stmt->bindParam(':dig_sign',$this->dig_sign);
            try{ 
                $stmt->execute();
                return true;
            }catch (exception $e){
                return false;
            }
        }

        public function update() {
            $query='UPDATE  '.$this->table. '
            SET
            title= :title,
            body= :body,
            author= :author,
            category_id= :category_id
            WHERE id= :id
            ';


            $stmt=$this->conn->prepare($query);

            $this->title=htmlspecialchars(strip_tags($this->title));
            $this->body=htmlspecialchars(strip_tags($this->body));
            $this->author=htmlspecialchars(strip_tags($this->author));
            $this->category_id=htmlspecialchars(strip_tags($this->category_id));
            $this->id=htmlspecialchars(strip_tags($this->id));


            $stmt->bindParam(':title', $this->title);
            $stmt->bindParam(':body', $this->body);
            $stmt->bindParam(':author', $this->author);
            $stmt->bindParam(':category_id', $this->category_id);
            $stmt->bindParam(':id', $this->id);

            if($stmt->execute()){
                return true;
            }

            printf("Error: %s\n",$stmt->error);
            return false;
        }

        public function delete() {

            $query = 'DELETE FROM ' . $this->table . ' WHERE id = :id';

            $stmt = $this->conn->prepare($query);


            $this->id = htmlspecialchars(strip_tags($this->id));


            $stmt->bindParam(':id', $this->id);


            if($stmt->execute()) {
                return true;
            }

            printf("Error: %s.\n", $stmt->error);

            return false;
        }
    }
