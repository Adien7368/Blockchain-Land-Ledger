<?php

header('Access-Control-Allow-Origin: *');
header('Control-Type: application/json ');
echo "hi";

include_once 'config/Database.php';

include_once 'models/Posts.php';

$database= new Database();
 

$db = $database->connect();
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