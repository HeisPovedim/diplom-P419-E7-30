<?php
session_start();
#подключение к базе данных
require_once("../db/db.php");
$db = new DB();
$link = $db->get_link();

$login = $_POST["login"];
$hashed_password = hash("sha256",$_POST['password']);

$personal = mysqli_query($link,"SELECT * FROM `personals` WHERE `login`='$login' AND `password`='$hashed_password'");
$personal = mysqli_fetch_assoc($personal);

if (empty($personal)){
    $_SESSION['err'] = 'Неверные данные';
    header("Location: ../auth_personal_page.php");
}else{
    if ($personal['access']){
        setcookie("idpers",$personal['idpersonals'],time()+28000,'/');
        header("Location: ../personal_page.php");
    }else{
        $_SESSION['err'] = 'Вы заблокированы, обратитесть к администратору';
        header("Location: ../auth_personal_page.php");
    }

}

?>