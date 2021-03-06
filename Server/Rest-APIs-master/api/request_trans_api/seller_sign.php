<?php
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');
header('Access-Control-Allow-Methods: PUT');
header('Access-Control-Allow-Headers: Access-Control-Allow-Headers,Content-Type,Access-Control-Allow-Methods, Authorization, X-Requested-With');

include_once '../../config/Database.php';
include_once '../../models/request_trans_model.php';

$database= new Database();

$db = $database->connect();

$post= new Post($db);

$data=json_decode(file_get_contents("php://input"));

$post->sell_hex=$data->sell_hex;
$post->land_id=$data->land_id;
$post->seller_id=$data->seller_id;
$post->buyer_id=$data->buyer_id;

// sign update
if($post->seller_sign()) {
    echo json_encode(
        array('message'=>'post updated')
    );
}
else{
    echo json_encode(
        array('message'=>'Post not updated')
    );
}

?>