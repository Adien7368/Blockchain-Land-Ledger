<?php
//headers
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

include_once '../../config/Database.php';
include_once '../../models/request_trans_model.php';

$database= new Database();

$db = $database->connect();

$post= new post($db);
$post->seller_id = isset($_GET['id'])? $_GET['id'] : die();
$result = $post->my_requests();

echo json_encode($result);

?>
