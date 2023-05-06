<?php
#подключение к базе данных
require_once("../db/db.php");
$db = new DB();
$link = $db->get_link();
error_reporting(E_ALL);
ini_set('display_errors', '1');


// Получение данных об объекте из таблицы objects
$object_id = $_POST['id_object']; // Пример id объекта
$select_obj = mysqli_query($link, "SELECT * FROM objects WHERE `idobjects` = '$object_id'");
$select_obj = mysqli_fetch_assoc($select_obj);

// Открытие файла для записи
$file = fopen('../reports/report.csv', 'w');

// Запись информации об объекте
fputcsv($file, array('Информация об объекте:'));
fputcsv($file, array('Имя:', $select_obj['name']));
fputcsv($file, array('Материал:', $select_obj['material']));
fputcsv($file, array('№ партии:', $select_obj['batch_number']));
fputcsv($file, array('Дата выпуска:', $select_obj['manufactured_date']));
fputcsv($file, array('Дата получения:', $select_obj['received_date']));
fputcsv($file, array('Длинна:', $select_obj['length']));
fputcsv($file, array('Ширина:', $select_obj['width']));
fputcsv($file, array('Толщина:', $select_obj['thickness']));

// Запись заголовков таблицы параметров
fputcsv($file, array('Результаты измерений:'));
fputcsv($file, array('id_parameters','Freq', 'z_parameters', 'phi_parameters', 'gp_parameters', 'rp_parameters', 'cp_parameters', 'measurement_date','id_personal'));

// Запись таблицы параметров данными из базы данных
$select_param = mysqli_query($link, "SELECT * FROM parameters WHERE `objects_idobjects` = '$object_id'");
$select_param = mysqli_fetch_all($select_param);
foreach ($select_param as $sp) {
    fputcsv($file, $sp);
}



// Отправка заголовков HTTP
header('Content-Type: text/csv');
header('Content-Disposition: attachment; filename="report.csv"');

// Отправка файла пользователю
readfile('../reports/report.csv');

// Удаление файла
unlink('../reports/report.csv');

// Закрытие файла
fclose($file);
?> 