<?php
session_start();
require_once("../db/db.php");
$db = new DB();
$link = $db->get_link();

$login = $_POST['login'];

$operator = mysqli_query($link,"SELECT * FROM `personals` WHERE `login`='$login'");
$operator = mysqli_fetch_assoc($operator);
$id = $operator['idpersonals'];

if (isset($operator)){
    $result = mysqli_query($link, "DELETE FROM `personals` WHERE `idpersonals` = '$id'");
    if (!$result) {
        var_dump('Ошибка удаления: ' . mysqli_error($link));
        var_dump($result);
    }
    var_dump($result);
    // $_SESSION['sucs'] = "Оператор успешно удален";
    // header("Location: ../admin_page.php");
}else{
    // $_SESSION['sucs'] = "Оператор не найден";
    // header("Location: ../admin_page.php");
}

?>