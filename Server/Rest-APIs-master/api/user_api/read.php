<?php
//headers
header('Access-Control-Allow-Origin: *');
header('Control-Type: application/json ');

include_once '../../config/Database.php';
include_once '../../models/user_model.php';

$database= new Database();

$db = $database->connect();

$post= new post($db);
$result = $post->read();
$num=$result->rowCount();

if($num>0){
    $posts_arr=array();
    $posts_arr['data']=array();

    while ($row=$result->fetch(PDO::FETCH_ASSOC)){
        extract($row);


        $post_item= array(

            'id'=>$id,
            'name'=>$name,
            'username'=>$user_name,
            'address'=>$address,
            'dob'=>$dob,
            'dig_sign'=>$dig_sign,
            'phone'=>$phone,
            'email'=>$email,
            'wallet_id'=>$wallet_id
        );
        array_push($posts_arr['data'],$post_item);
    }

    echo json_encode($posts_arr);
}

else{
    echo json_encode(
        array('message'=>'No Post found')
    );

}
