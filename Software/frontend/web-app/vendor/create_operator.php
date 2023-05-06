<?php
session_start();
#подключение к базе данных
require_once("../db/db.php");
$db = new DB();
$link = $db->get_link();

var_dump($_POST);

$login = $_POST["login"];
$hashed_password = hash("sha256",$_POST['password']);
$fio = $_POST['fio'];

$personal = mysqli_query($link,"SELECT * FROM `personals` WHERE `login`='$login'");
$personal = mysqli_fetch_assoc($personal);

$date = date("Y-m-d");
$id_admin = (int)$_COOKIE["idadm"];

if(empty($personal)){
    mysqli_query($link,"INSERT INTO `personals`
                        (`fio`,`login`,`password`,`data_created`,`admins_idadmins`)
                        VALUES
                        ('$fio','$login','$hashed_password','$date', '$id_admin')
    ");
    $_SESSION['sucs'] = 'Оператор добавлен';
    header("Location: ../admin_page.php");

}else{
    $_SESSION['err'] = 'Логин занят';
    header("Location: ../admin_page.php");
}

?>