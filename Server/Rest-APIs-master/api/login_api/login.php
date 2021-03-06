<?php
//headers
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Access-Control-Allow-Headers,Content-Type,Access-Control-Allow-Methods, Authorization, X-Requested-With');

include_once '../../config/Database.php';
include_once '../../models/login_model.php';

$database= new Database();

$db = $database->connect();

$post= new post($db);

$data=json_decode(file_get_contents("php://input"));

$post->user_name=$data->user_name;
$post->user_pass=$data->user_pass;

$result = $post->validate();
if($result==0){
    echo json_encode(
        array('message'=>'user doesnt exist')
    );
}

else if($result==1){    echo json_encode(
        array('message'=>'success')
    );
}

else{
    echo json_encode(
        array('message'=>'fail')
    );

}