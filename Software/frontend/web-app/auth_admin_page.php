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
    <link rel="stylesheet" href="./css/index.css">
</head>
<body>
    <header>
        <div class="header-container">
            <a href="./index.php"><img src="./assets/img/logo.svg" alt="logo"></a>
        </div>
    </header>
    <div class="container admin-auth">
        <span>Администратор</span>
        <form action="./vendor/auth_admin.php" method="post">
            <div class="admin-auth__login">
                <input type="text" class="admin-auth-form__field" placeholder="Логин" name="login" id='name' required />
                <label for="name" class="admin-auth-form__label">Логин</label>
            </div>
            <div class="admin-auth__password">
                <input type="password" class="admin-auth-form__field" placeholder="Пароль" name="password" id='name' required />
                <label for="name" class="admin-auth-form__label">Пароль</label>
            </div>
            <div class="admin-auth__buttons">
                <button>Войти</button>
                <a href="./index.php">Назад</a>
            </div>
        </form>
    </div>
</body>
</html>