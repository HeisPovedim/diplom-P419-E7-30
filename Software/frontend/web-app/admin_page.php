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
    <link rel="stylesheet" href="./css/index.css">
</head>
<body>
    <header>
        <div class="header-container admin-header">
            <a href="./index.php"><img src="./assets/img/logo.svg" alt="logo"></a>
            <div class="admin-header__info-user">
                <span>Логин: <?= $admin['login']?></span>
                <a href="./logout.php">Выйти</a>
            </div>
        </div>
    </header>
    <div class="container admin-page">
        <div class="admin-page__add-user">
            <span style="font-weight: 600">Добавить оператора</span>
            <form action="./vendor/create_operator.php" method="post">
                <input type="text" name="login" placeholder="Логин" required />
                <input type="password" name="password" placeholder="Пароль" required />
                <input type="text" name="fio" placeholder="ФИО" required />
                <button>Добавить оператора</button>
            </form>
        </div>

        <div class="admin-page__add-user">
            <span style="font-weight: 600">Заблокировать оператора</span>
            <form action="./vendor/block_operator.php" method="post">
                <input type="text" name="login" placeholder="Введите логин оператора" required />
                <button>Блокировать</button>
            </form>
        </div>

        <div class="admin-page__add-user">
            <span style="font-weight: 600">Разблокировать оператора</span>
            <form action="./vendor/unblock_operator.php" method="post">
                <input type="text" name="login" placeholder="Введите логин оператора" required />
                <button>Разблокировать</button>
            </form>
        </div>

        <h4>Просмотреть историю взаимодействия с прибором</h4>
        <a href="./view_object_page.php">Открыть историю</a>
    </div>
</body>
</html>