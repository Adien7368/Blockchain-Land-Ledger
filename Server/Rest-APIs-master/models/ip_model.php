<?php
     class Post {
        private $conn;
        private $table='ip';

        public $id;
        public $address;

        public function __construct($db){
            $this->conn=$db;
        }
        
        public function read(){
            $query='SELECT * FROM ip';
            $stmt=$this->conn->prepare($query);
            $stmt->execute();
            return $stmt;
        }

        public function register() {
            $query='SELECT * FROM ip where id=:id';
            $stmt=$this->conn->prepare($query);
            $stmt->bindParam('id', $this->id);
            $stmt->execute();
            if($stmt->rowCount()>0)return 0;
            $query='INSERT INTO ip (id, address) VALUES (:id,:address)';
            $stmt=$this->conn->prepare($query);
	        $stmt->bindParam(':id', $this->id);
            $stmt->bindParam(':address', $this->address);
            if($stmt->execute()){
                return 1;
            }else{
		        return 0;
	        }
        }

        public function delete(){
            $query='DELETE FROM ip WHERE id=:id';
            $stmt=$this->conn->prepare($query);
            $stmt->bindParam(':id', $this->id);
            if($stmt->execute()){
		        return 1;
	        }else{
		        return 0;
            }
       }
   }



?>
