<?php
     class Post {
        private $conn;
        private $table='login';

        public $id;
        public $u_id;
        public $name;
        public $email;
        public $id_no;
        public $address;
        public $phone;
        public $dig_sign;
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
            $quer='SELECT * FROM user where user_name=:user_name';
            $stmt=$this->conn->prepare($query);
            $stm=$this->conn->prepare($quer);
            $stmt->bindParam('user_name', $this->user_name);
            $stm->bindParam('user_name', $this->user_name);
            $stmt->execute();
            $stm->execute();
            
            if($stmt->rowCount()>0 || $stm->rowCount()>0)return 0;
            
            $query='INSERT INTO user
            SET
            name= :name,
            email= :email,
            address= :address,
            phone= :phone,
            wallet_id=22,
            dig_sign="null",
            dob="null",
            user_name= :user_name
            ';

            $query1='INSERT INTO login
            SET
            user_id=:user_id,
            user_name= :user_name,
            user_pass= :user_pass
            ';

            $stmt=$this->conn->prepare($query);
            $stmt->bindParam(':name', $this->name);
            $stmt->bindParam(':email', $this->email);
            // $stmt->bindParam(':id_no', $this->id_no);
            $stmt->bindParam(':address', $this->address);
            $stmt->bindParam(':phone', $this->phone);
            $stmt->bindParam(':user_name', $this->user_name);

            $stmt->execute();
            // echo $stmt->rowCount()."   ";


            $que='SELECT * FROM user where user_name=:user_name';
            $st=$this->conn->prepare($que);
            $st->bindParam(':user_name', $this->user_name);
            $st->execute();
            $result = $st->fetch(PDO::FETCH_ASSOC);
            // extract($result);
            // echo $result['id'];
            $this->u_id=$result['id'];

            $stmt1=$this->conn->prepare($query1);
            $stmt1->bindParam(':user_id', $this->u_id);
            $stmt1->bindParam(':user_name', $this->user_name);
            $stmt1->bindParam(':user_pass', $this->user_pass);
            
            if($stmt1->execute()){
                return 1;
            }
            else {
                return 0;
            }
        }

}



