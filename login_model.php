<?php
     class Post {
        private $conn;
        private $table='login';

        public $name;
        public $email;
        public $id_no;
        public $address;
        public $phone;
        public $user_id;
        public $user_name;
        public $user_pass;

        public function __construct($db)
        {
            $this->conn=$db;
        }

        public function validate() {
            $query='SELECT * FROM login where user_name=:user_name';
            $stmt=$this->conn->prepare($query);
             $stmt->bindParam('user_name', $this->user_name);
            $stmt->execute();

            if($stmt->rowCount()<=0)return 0;

            $query1='SELECT * FROM login where user_name=:user_name and user_pass=:user_pass limit 1';
            $stmt1=$this->conn->prepare($query1);
            $stmt1->bindParam('user_name', $this->user_name);
            $stmt1->bindParam('user_pass', $this->user_pass);
            $stmt1->execute();
            if($stmt1->rowCount()>0)return 1;
            else return 2;   
        }

        public function register() {
            $query='SELECT * FROM login where user_name=:user_name';
            $stmt=$this->conn->prepare($query);
             $stmt->bindParam('user_name', $this->user_name);
            $stmt->execute();

            if($stmt->rowCount()>0)return 0;

            
            $query='INSERT INTO user
            SET
            name=> :name,
            email=> :email,
            id_no=> :id_no,
            address=> :address,
            phone=> :phone,
            wallet_id=null,
            no_of_lands=null,
            land_ids=null,
            dig_sign=null,
            dob=null,
            user_name= :user_name
            ';

            $query1='INSERT INTO login
            SET
            user_name= :user_name,
            user_pass= :user_pass
            ';


            $stmt=$this->conn->prepare($query);
            $stmt1=$this->conn->prepare($query1);

            // $this->title=htmlspecialchars(strip_tags($this->user_pass));
            // $this->body=htmlspecialchars(strip_tags($this->user_name));
            $stmt->bindParam(':name', $this->name);
            $stmt->bindParam(':email', $this->email);
            $stmt->bindParam(':id_no', $this->id_no);
            $stmt->bindParam(':address', $this->address);
            // $stmt->bindParam(':dob', null);
            $stmt->bindParam(':phone', $this->phone);
            $stmt->bindParam(':user_name', $this->user_name);
            $stmt->bindParam(':user_pass', $this->user_pass);

            $stmt1->bindParam(':user_name', $this->user_name);
            $stmt1->bindParam(':user_pass', $this->user_pass);

            if($stmt1->execute()){
                return 1;
            }
            else return 0;

        }

    }



