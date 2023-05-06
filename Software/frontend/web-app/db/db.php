<?php

class DB{
    private $host = "localhost";
    private $user = "lorean";
    private $password = "1234";
    private $database = "diplom";

     public function get_link()
    {
        # code...
        $link = mysqli_connect($this->host,$this->user,$this->password,$this->database);
        return $link;
    }
}
?>