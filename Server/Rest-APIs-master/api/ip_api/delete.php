<?php
//headers
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

include_once '../../config/Database.php';
include_once '../../models/ip_model.php';

$database= new Database();

$db = $database->connect();

$post= new post($db);

$data = json_decode(file_get_contents("php://input"));

$post->id = $data->id;

$result = $post->delete();


if($result>0){
    echo json_encode(array('message'=>'success'));
}else{
    echo json_encode(array('message'=>'error not deleted'));
}



?>

