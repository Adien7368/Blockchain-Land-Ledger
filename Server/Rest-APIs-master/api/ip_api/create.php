<?php

header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Access-Control-Allow-Headers,Content-Type,Access-Control-Allow-Methods, Authorization, X-Requested-With');

include_once '../../config/Database.php';
include_once '../../models/ip_model.php';

$database= new Database();

$db = $database->connect();

$post= new Post($db);

$data=json_decode(file_get_contents("php://input"));

$post->id=$data->id;
$post->address=$data->address;


// create post
if($post->register()) {
    echo json_encode(
        array('message'=>'success')
    );
}
  else{
      echo json_encode(
          array('message'=>'Post not created')
      );
}

?>


