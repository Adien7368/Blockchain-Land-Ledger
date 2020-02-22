<?php

     class Post {
        private $conn;
        private $table='wallet';

        public $wallet_id;
        public $user_id;
        public $balance;
        public $saved_cards;
        public $transactions;

        public function __construct($db)
        {
            $this->conn=$db;
        }

        public function read(){
            $query='SELECT * FROM wallet';
            $stmt=$this->conn->prepare($query);
            $stmt->execute();
            return $stmt;
        }

        public function read_single() {
            $query='SELECT * FROM wallet where wallet_id=:wallet_id limit 1';
            $stmt=$this->conn->prepare($query);
             $stmt->bindParam('wallet_id', $this->wallet_id);
            $stmt->execute();
            return $stmt;   
        }

        // create post

        public function create() {
            $query='INSERT INTO '.$this->table. '
            SET
            title= :title,
            body= :body,
            author= :author,
            category_id= :category_id
            ';


            $stmt=$this->conn->prepare($query);

            $this->title=htmlspecialchars(strip_tags($this->title));
            $this->body=htmlspecialchars(strip_tags($this->body));
            $this->author=htmlspecialchars(strip_tags($this->author));
            $this->category_id=htmlspecialchars(strip_tags($this->category_id));

            $stmt->bindParam(':title', $this->title);
            $stmt->bindParam(':body', $this->body);
            $stmt->bindParam(':author', $this->author);
            $stmt->bindParam(':category_id', $this->category_id);

            if($stmt->execute()){
                return true;
            }

            printf("Error: %s\n",$stmt->error);
            return false;

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