<?php
//headers
header('Access-Control-Allow-Origin: *');
header('Control-Type: application/json ');

include_once '../../config/Database.php';
include_once '../../models/land_model.php';

$database= new Database();

$db = $database->connect();

$post= new post($db);
$post->land_id=isset($_GET['land_id'])? $_GET['land_id'] : die();
$result = $post->read_single();
$num=$result->rowCount();
// echo($num);

if($num>0){
    $posts_arr=array();
    $posts_arr['data']=array();

    if ($row=$result->fetch(PDO::FETCH_ASSOC)){
        extract($row);
        $post_item= array(
            'land_id'=>$land_id,
            'inspector_id'=>$inspector_id,
            'address'=>$address,
            'documents'=>$documents,
            'coordinates'=>$coordinates,
            'area'=>$area,
            'message'=>'success'
        );
	echo json_encode($post_item);
        //array_push($posts_arr['data'],$post_item);
    }

    //echo json_encode($posts_arr);
}

else{
    echo json_encode(
        array('message'=>'No Post found')
    );

}
