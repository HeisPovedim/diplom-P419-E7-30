<?php
session_start();
require_once("./models/log.php");
if(empty($_COOKIE['idpers'])){
    $_SESSION['err'] = 'Авторизуйтесь как оператор';
    header("Location: ./auth_personal_page.php");
}else{
    require_once("./db/db.php");
    session_destroy();

    $id = $_COOKIE['idpers'];
    $db = new DB();
    $link = $db->get_link();

    $personal = mysqli_query($link,"SELECT `login` FROM `personals` WHERE `idpersonals`='$id'");
    $personal = mysqli_fetch_assoc($personal);
}


?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/index.css">
    <title>Кабинет оператора</title>
</head>
<body>
    <h4>Добро пожаловать: <?= $personal['login'] ?></h4>
    <a href="./logout.php">Выйти</a>
    <h4>Правила работы с прибором</h4>

    <h4>Добавление исследуемого объекта</h4>
    <div>
        <form action="./vendor/create_object.php" method="post" class="form_post_data">
            <input type="text" name="name" placeholder="Название объекта" required/>
            <input type="text" name="material" placeholder="Материал" required/>
            <input type="text" name="batch_number" placeholder="Номер партии" required/>
            <label for="manufactured_date">Дата производства</label>
            <input type="date" name="manufactured_date" placeholder="Дата производства" required/>
            <label for="received_date">Дата получения</label>
            <input type="date" name="received_date" placeholder="Дата получения" required/>
            <input type="text" name="length" placeholder="Длинна" required/>
            <input type="text" name="width" placeholder="Ширина" required/>
            <input type="text" name="thickness" placeholder="Толщина" required/>
            <input type="hidden" name="personals_idpersonals" value="<?= $_COOKIE["idpers"]; ?>"/>

            <button>Добавить</button>
        </form>
    </div>
    <h4>Просмотреть историю взаимодействия с прибором</h4>
    <a href="./view_object_page.php">Открыть историю</a>
</body>
</html>