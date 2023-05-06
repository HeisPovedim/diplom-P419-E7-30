<?php

if(empty($_SESSION['err'])){
    echo "";
}else{
    echo $_SESSION['err'];
}
if(empty($_SESSION['sucs'])){
    echo "";
}else{
    echo $_SESSION['sucs'];
}