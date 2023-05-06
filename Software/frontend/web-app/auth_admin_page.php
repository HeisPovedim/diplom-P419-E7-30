<?php
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
</head>
<body>
    <h4>Вход администратора</h4>
    <form action="./vendor/auth_admin.php" method="post">
        <input type="text" name="login" required placeholder="Логин">
        <input type="password" name="password" required placeholder="Пароль">
        <button>Войти</button>
    </form>
    <a href="./index.php">Назад</a>
</body>
</html>