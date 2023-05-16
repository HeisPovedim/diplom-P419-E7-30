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
    <div class="container personal-auth">
        <span>Пользователь</span>
        <form action="./vendor/auth_personal.php" method="post">
            <div class="personal-auth__login">
                <input type="text" class="personal-auth-form__field" placeholder="Логин" name="login" id='name' required />
                <label for="name" class="personal-auth-form__label">Логин</label>
            </div>
            <div class="personal-auth__password">
                <input type="password" class="personal-auth-form__field" placeholder="Пароль" name="password" id='name' required />
                <label for="name" class="personal-auth-form__label">Пароль</label>
            </div>
            <div class="personal-auth__buttons">
                <button>Войти</button>
                <a href="./index.php">Назад</a>
            </div>
        </form>
    </div>
</body>
</html>