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
</head>
<body>
    <a href="./auth_admin_page.php">Вход для администратора</a><br>
    <a href="./auth_personal_page.php">Вход для персонала</a><br>
</body>
</html>