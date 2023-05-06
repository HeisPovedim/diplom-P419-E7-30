<?php 
session_start();
require_once("../db/db.php");
$db = new DB();
$link = $db->get_link();
$id_object = (int)$_POST['id_object'];

setcookie("id_object",$id_object,time()+1000,'/');
header("Location: ../view_parameters_page.php");

?>