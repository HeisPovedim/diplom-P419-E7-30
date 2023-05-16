<?php
session_start();
require_once("../db/db.php");
$db = new DB();
$link = $db->get_link();

$login = $_POST['login'];

$operator = mysqli_query($link,"SELECT * FROM `personals` WHERE `login`='$login'");
$operator = mysqli_fetch_assoc($operator);
$id = $operator['idpersonals'];

if (($operator['access'])){

    $_SESSION['sucs'] = "Оператор не заблокирован";
    header("Location: ../admin_page.php");
}else{
    $operator = mysqli_query($link,"UPDATE `personals` SET `access` = '1' WHERE (`idpersonals` = '$id');");
    $_SESSION['sucs'] = "Оператор разблокирован";
    header("Location: ../admin_page.php");
}

?>