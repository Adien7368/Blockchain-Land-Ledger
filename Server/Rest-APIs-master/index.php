<?php

header('Access-Control-Allow-Origin: *');
header('Control-Type: application/json ');

include_once 'config/Database.php';

include_once 'models/Posts.php';

$database= new Database();
 

$db = $database->connect();
<<<<<<< HEAD

if($db){
	echo "string";
}
else
{
	echo "ddkje";
}

// $post= new post($db);
// $result = $post->read();
// $num=$result->rowCount();


?>
