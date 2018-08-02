<?php 

$texto = $_POST["texto"];

error_reporting(E_ALL);

/* Add redirection so we can get stderr. */
$handle = popen('python.exe C:\\wamp64\\www\\php-python\\3insere-bd.py -a ' . $texto, 'r');
echo "'$handle'; " . gettype($handle) . "\n";
$read = fread($handle, 2096);
var_dump($read);
pclose($handle);

?>