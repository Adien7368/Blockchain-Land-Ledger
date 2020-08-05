<?php
     class Post {
        private $conn;
        private $table='request_transaction';


        public $price;
        public $land_id;
        public $seller_id;
        public $buyer_id;
        public $inspector_id;
        public $buy_hex;
        public $sell_hex;
        public $inspector_hex;
        public $documents;


        public function __construct($db){
            $this->conn=$db;
        }

        public function read(){
            $query='SELECT * FROM request_transaction';
            $stmt=$this->conn->prepare($query);
            $stmt->execute();
            return $stmt;
        }

        public function my_requests(){
            $query='SELECT * FROM request_transaction WHERE seller_id=:seller_id';
            $stmt=$this->conn->prepare($query);
            $stmt->bindParam(':seller_id',$this->seller_id);
	    $stmt->execute();
            return $stmt;
        }

        public function seller_sign(){
            $query='UPDATE request_transaction SET sell_hex=:sell_hex WHERE land_id=:land_id AND seller_id=:seller_id AND buyer_id=:buyer_id';
            $stmt=$this->conn->prepare($query);
            $stmt->bindParam(':land_id', $this->land_id);
            $stmt->bindParam(':seller_id', $this->seller_id);
            $stmt->bindParam(':buyer_id', $this->buyer_id);
            $stmt->bindParam(':sell_hex', $this->sell_hex);
            
            if($stmt->execute()){
                return 1;
            }else{
                return 0;
            }
            return $stmt;
        }

        public function inspector_sign(){
            $query='UPDATE request_transaction SET inspector_hex=:inspector_hex WHERE land_id=:land_id AND seller_id=:seller_id AND buyer_id=:buyer_id';
            $stmt=$this->conn->prepare($query);
            $stmt->bindParam(':land_id', $this->land_id);
            $stmt->bindParam(':seller_id', $this->seller_id);
            $stmt->bindParam(':buyer_id', $this->buyer_id);
            $stmt->bindParam(':inspector_hex', $this->inspector_hex);
            
            if($stmt->execute()){
                return 1;
            }else{
                return 0;
            }
            return $stmt;
        }


        public function register() {

            $query='INSERT INTO request_transaction ( price, land_id, seller_id, buyer_id, buy_hex, sell_hex, documents ) VALUES (:price,:land_id,:seller_id,:buyer_id,:buy_hex,:sell_hex,:documents)';
            $stmt=$this->conn->prepare($query);
	    $stmt->bindParam(':price', $this->price);
            $stmt->bindParam(':land_id', $this->land_id);
            $stmt->bindParam(':seller_id', $this->seller_id);
            $stmt->bindParam(':buyer_id', $this->buyer_id);
            $stmt->bindParam(':buy_hex', $this->buy_hex);
            $stmt->bindParam(':sell_hex', $this->sell_hex);
            $stmt->bindParam(':documents', $this->documents);
            if($stmt->execute()){
                return 1;
            }else{
	        return 0;
            }
        }

        public function delete(){
            $query='DELETE FROM request_transaction WHERE land_id=:land_id AND seller_id=:seller_id AND buyer_id=:buyer_id';
            $stmt=$this->conn->prepare($query);
            $stmt->bindParam(':land_id', $this->land_id);
            $stmt->bindParam(':seller_id', $this->seller_id);
            $stmt->bindParam(':buyer_id', $this->buyer_id);

            if($stmt->execute()){
		        return 1;
	        }else{
		        return 0;
            }
       }
   }



?>
