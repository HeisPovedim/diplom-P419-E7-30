<?php
session_start();
#подключение к базе данных
require_once("../db/db.php");
$db = new DB();
$link = $db->get_link();

$login = $_POST["login"];
$hashed_password = hash("sha256",$_POST['password']);

$admin = mysqli_query($link,"SELECT * FROM `admins` WHERE `login`='$login' AND `password`='$hashed_password'");
$admin = mysqli_fetch_assoc($admin);

if (empty($admin)){
    $_SESSION['err'] = 'Неверные данные';
    header("Location: ../auth_admin_page.php");
}else{
    setcookie("idadm",$admin['idadmins'],time()+28000,'/');
    header("Location: ../admin_page.php");
}



?>