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
	$query='INSERT INTO posts
            SET
            title= "njsjfnj"
            ';

            $stmt=$this->conn->prepare($query);

            $stmt->execute();
}
else
{
	echo "ddkje";
}

// $post= new post($db);
// $result = $post->read();
// $num=$result->rowCount();


?>