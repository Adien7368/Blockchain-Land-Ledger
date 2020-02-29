<?php
//headers
header('Access-Control-Allow-Origin: *');
header('Control-Type: application/json ');

include_once '../../config/Database.php';
include_once '../../models/user_model.php';

$database= new Database();

$db = $database->connect();


    private $host ='localhost:3306';
    private $db_name='ledger';
    private $username = 'sammy';
    private $password='1@9!9458';


$post= new post($db);
$post->user_name=isset($_GET['user_name'])? $_GET['user_name'] : die();
$result = $post->read_user();
$num=$result->rowCount();
if($num>0){

    //$posts_arr=array();
    //$posts_arr['data']=array();

    if($row=$result->fetch(PDO::FETCH_ASSOC)){
        extract($row);
        $post_item= array(

            'id'=>$id,
            'name'=>$name,
            'address'=>$address,
            'dob'=>$dob,
            'dig_sign'=>$dig_sign,
            'phone'=>$phone,
            'email'=>$email,
            'wallet_id'=>$wallet_id,
            'user_name'=>$user_name,
            'message'=>'success'

        );
        //array_push($posts_arr['data'],$post_item);
   	echo json_encode($post_item); 
   }
    //echo json_encode($posts_arr);
}
else{
    echo json_encode(
        array('message'=>'User Name not found')
    );

}
