<?php
require_once("./router/redirect_index_to_home.php");
session_start();
require_once("./models/log.php");
session_destroy();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Программно-аппаратный комплекс для работы с Е7-30</title>
    <link rel="stylesheet" href="./css/index.css">
</head>
<body>
    <header>
        <div class="header-container">
            <a href="./index.php"><img src="./assets/img/logo.svg" alt="logo"></a>
        </div>
    </header>
    <div class="container input-type">
        <span>АВТОРИЗАЦИЯ</span>
        <div class="input-type__content">
            <a href="./auth_admin_page.php"><span>Вход для администратора</span></a><br>
            <a href="./auth_personal_page.php"><span>Вход для персонала</span></a>
        </div>
    </div>
</body>
</html>