<?php

header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Access-Control-Allow-Headers,Content-Type,Access-Control-Allow-Methods, Authorization, X-Requested-With');

include_once '../../config/Database.php';
include_once '../../models/request_trans_model.php';

$database= new Database();

$db = $database->connect();

$post= new Post($db);

$data=json_decode(file_get_contents("php://input"));
$post->price=$data->price;
$post->land_id=$data->land_id;
$post->seller_id=$data->seller_id;
$post->buyer_id=$data->buyer_id;
$post->inspector_id=$data->inspector_id;
$post->buy_hex=$data->buy_hex;
$post->sell_hex=$data->sell_hex;
$post->inspector_hex=$data->inspector_hex;
$post->documents=$data->documents;


// create 
if(($post->register())>0) {
    echo json_encode(array('message'=>'success:request created'));
}else{
    echo json_encode(array('message'=>'request not created'));
}

?>
