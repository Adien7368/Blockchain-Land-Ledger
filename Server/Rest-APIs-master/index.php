<?php

header('Access-Control-Allow-Origin: *');
header('Control-Type: application/json ');

include_once 'config/Database.php';

include_once 'models/Posts.php';

$database= new Database();
 

$db = $database->connect();
<<<<<<< HEAD

if($db){
	echo "strg";
=======
if($db){
	echo "string";
>>>>>>> 3384ade34f35df9f8b1aabaa17aa050f0b93f855
}
else
{
	echo "ddkje";
}

// $post= new post($db);
// $result = $post->read();
// $num=$result->rowCount();


?>