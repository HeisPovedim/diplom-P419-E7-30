<?php
session_start();
require_once("./models/log.php");
if(empty($_COOKIE['idadm'])){
    $_SESSION['err'] = 'Авторизуйтесь как администратор';
    header("Location: ./auth_admin_page.php");
}else{
    require_once("./db/db.php");
    session_destroy();
    $id = $_COOKIE['idadm'];
    $db = new DB();
    $link = $db->get_link();

    $admin = mysqli_query($link,"SELECT `login` FROM `admins` WHERE `idadmins`='$id'");
    $admin = mysqli_fetch_assoc($admin);
}


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/index.css">
    <title>Кабинет администратора</title>
</head>
<body>
<h4>Добро пожаловать: <?= $admin['login']?></h4>
    <a href="./logout.php">Выйти</a>
    <h4>Добавить оператора</h4>
    <form action="./vendor/create_operator.php" method="post">
        <input type="text" name="login" placeholder="Логин" required>
        <input type="password" name="password" placeholder="Пароль" required>
        <input type="text" name="fio" placeholder="ФИО" required>
        <button>Добавить оператора</button>
    </form>
    <h4>Просмотреть историю взаимодействия с прибором</h4>
    <a href="./view_object_page.php">Открыть историю</a>
</body>
</html>