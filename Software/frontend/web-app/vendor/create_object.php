<?php
session_start();
#подключение к базе данных
require_once("../db/db.php");
$db = new DB();
$link = $db->get_link();

$name = $_POST['name'];
$material = $_POST['material'];
$batch_number = $_POST['batch_number'];
$manufactured_date = $_POST['manufactured_date'];
$received_date = $_POST['received_date'];
$length = $_POST['length'];
$width = $_POST['width'];
$thickness = $_POST['thickness'];
$personals_idpersonals = $_POST['personals_idpersonals'];

$select_obj = mysqli_query($link, "SELECT * FROM `objects` WHERE `name` = '$name'");
$select_obj = mysqli_fetch_assoc($select_obj);

if(empty($select_obj)) {
    mysqli_query($link, "INSERT INTO `objects`
                        (`name`, `material`, `batch_number`, `manufactured_date`, `received_date`, `length`, `width`, `thickness`, `personals_idpersonals`) 
                        VALUES 
                        ('$name','$material','$batch_number','$manufactured_date','$received_date','$length','$width','$thickness','$personals_idpersonals')
    ");

    $_SESSION['sucs'] = "Успешно добавлен объект!";
} else {
    $_SESSION['err'] = "Объект с таким названием, уже существует!";
}

header("Location: " . $_SERVER['HTTP_REFERER']);
?>