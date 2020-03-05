<?php
//headers
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

include_once '../../config/Database.php';
include_once '../../models/ip_model.php';

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
            'address'=>$address
        );
        array_push($posts_arr['data'],$post_item);
    }
    echo json_encode($posts_arr['data']);
}else{
    echo json_encode('{}');
}



?>
