<?php
if(isset($_COOKIE['idadm'])){
    header("Location: ../admin_page.php");
}else if(isset($_COOKIE['idpers'])){
    header("Location: ../personal_page.php");
}
?>