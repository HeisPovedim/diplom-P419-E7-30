<?php
session_start();
if(empty($_COOKIE['idadm']) && empty($_COOKIE['idpers'])){
    $_SESSION['err'] = 'Пройдите авторизацию';
    header("Location: ./index.php");
}else{
    
    require_once("./db/db.php");
    require_once("./models/log.php");
    session_destroy();
    //получение данных из БД

    $db = new DB();
    $link = $db->get_link();
    $objects = mysqli_query($link,"SELECT `o`.*, `pers`.`login`
                                FROM `objects` `o`
                                JOIN `personals` `pers` ON `pers`.`idpersonals`=`o`.`personals_idpersonals`
                                ORDER BY `o`.`idobjects` DESC");
    $objects = mysqli_fetch_all($objects);

}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/view.css">
    <title>Просмотр исследуемых объектов</title>
</head>
<body>
    <h4>Данные:</h4>
    <div class="parameters_block">
    <?php
    if(empty($objects)){
        echo "В базе данных отсутсвует информация о взаимодействии с прибором";
    }else{ 
        foreach ($objects as $o){ ?>
        <div class="element" onmouseenter="showCalcBlock(this)" onmouseleave="hideCalcBlock(this)">
            <span>Порядковый номер объекта: <?= $o[0]?></span>
            <span>Наименование объекта: <?= $o[1]?></span>
            <span>Материал: <?= $o[2]?></span>
            <span>Номер партии: <?= $o[3]?></span>
            <span>Дата производства: <?= $o[4]?></span>
            <span>Длинна: <?= $o[5]?></span>
            <span>Ширина: <?= $o[6]?></span>
            <span>Толщина: <?= $o[7]?></span>
            <span>Имя оператора добавивший объект: <?= $o[10]?></span>
            <form action="./vendor/create_report.php" method="post">
                <input type="hidden" name="id_object" value="<?= $o[0]?>">
                <button>Скачать отчет</button>
            </form>

            <?php if(empty($_COOKIE['idpers'])){
                echo '';
            }else{ ?>
            <div class="calc_block" style="display: none;">
            <h4>Сформировать запрос на вычисление параметров данного объекта</h4>
                <form action="./vendor/calc_parameters.php" method="post">
                    <input type="text" name="id_object"  value="<?= $o[0]?>" hidden>
                    <input type="text" name="f_start" pattern="[0-9]*" maxlength="30" placeholder="начальная частота" required>
                    <input type="text" name="f_end" pattern="[0-9]*" maxlength="30" placeholder="конечная частота" required>
                    <input type="text" name="step" required pattern="[0-9]*" maxlength="30" placeholder="шаг" required>
                    <label for="step">Получить измерения только последовательной схемы </label> 
                    <input type="checkbox" name="z_only"> <br> <br>
                    <button>Измерить параметры</button>
                </form>
            </div>
            <?php  } ?>
        </div>
       <?php }
    } ?>
                    
    </div> <br>
    <a href="./router/redirect_parameter_to_home.php">Назад</a>
    <script>
        function showCalcBlock(element) {
            var calcBlock = element.querySelector(".calc_block");
            if (calcBlock) {
                calcBlock.style.display = "block";
            }
        }
        function hideCalcBlock(element) {
            var calcBlock = element.querySelector(".calc_block");
            if (calcBlock) {
                calcBlock.style.display = "none";
            }
        }
</script>
</body>
</html>