<?php

     class Post {
        private $conn;
        private $table='land';

        public $land_id;
        public $owner_id;
        public $address;
        public $documents;
        public $coordinates;
        public $availability;
        public $inspector;

        public function __construct($db)
        {
            $this->conn=$db;
        }

        public function read(){
            $query='SELECT * FROM land';
            $stmt=$this->conn->prepare($query);
            $stmt->execute();
            return $stmt;
        }

        public function read_single() {
            // echo("   jhj".$this->land_id);
            $query='SELECT * FROM land where land_id=:land_id limit 1';
            $stmt=$this->conn->prepare($query);
            //echo "string";
            
            $stmt->bindParam('land_id', $this->land_id);
            $stmt->execute();
            //echo($stmt->rowCount());
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