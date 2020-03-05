<?php

header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Access-Control-Allow-Headers,Content-Type,Access-Control-Allow-Methods, Authorization, X-Requested-With');

include_once '../../config/Database.php';
include_once '../../models/user_model.php';

$database= new Database();

$db = $database->connect();

$post= new Post($db);

$data=json_decode(file_get_contents("php://input"));
$post->id=$data->id;
$post->user_name=$data->user_name;
$post->name=$data->name;
$post->email=$data->email;
$post->wallet_id=$data->wallet_id;
$post->phone=$data->phone;
$post->address=$data->address;
$post->dob=$data->dob;
$post->dig_sign=$data->dig_sign;

// create post
if(($post->create())>0) {
    echo json_encode(array('message'=>'success:user created'));
}else{
    echo json_encode(array('message'=>'user not created'));
}

?>
