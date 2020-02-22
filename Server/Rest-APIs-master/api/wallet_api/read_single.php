<?php
//headers
header('Access-Control-Allow-Origin: *');
header('Control-Type: application/json ');

include_once '../../config/Database.php';
include_once '../../models/wallet_model.php';

$database= new Database();

$db = $database->connect();

$post= new post($db);
$post->wallet_id=isset($_GET['wallet_id'])? $_GET['wallet_id'] : die();
$result = $post->read_single();
$num=$result->rowCount();
if($num>0){
    $posts_arr=array();
    $posts_arr['data']=array();

    while ($row=$result->fetch(PDO::FETCH_ASSOC)){
        extract($row);
        $post_item= array(

            'wallet_id'=>$wallet_id,
            'user_id'=>$user_id,
            'balance'=>$balance,
            'saved_cards'=>$saved_cards,
            'transactions'=>$transactions

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