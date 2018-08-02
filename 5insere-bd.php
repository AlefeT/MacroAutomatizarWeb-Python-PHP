<?php 

$name = $_POST["name"];

$db = mysqli_connect("db.db.db.db.db", "db", "db", "db");
mysqli_query($db, "INSERT INTO db.tabela (coluna) VALUES ('$name')");

?>

