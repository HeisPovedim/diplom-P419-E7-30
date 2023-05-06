<?php
session_start();
#подключение к базе данных
require_once("../db/db.php");
$db = new DB();
$link = $db->get_link();

$id_parameter = (int)$_POST['id_parameter'];

mysqli_query($link,"DELETE FROM `parameters` WHERE `idparameters`='$id_parameter'");
$_SESSION['sucs'] = 'Данные об ' . $id_admin . 'вычисление в базе данных удалены!';
header("Location: ../view_object_page.php");




?>