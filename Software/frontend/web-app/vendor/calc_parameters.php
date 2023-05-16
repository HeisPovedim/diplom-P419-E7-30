<?php


session_start();
#подключение к базе данных
require_once("../db/db.php");
require_once("../lib/phpMatch/tests/bootstrap.php");

$db = new DB();
$link = $db->get_link();

$id_object = $_POST["id_object"];

$f_start = $_POST["f_start"];
$f_end = $_POST["f_end"];
$step = $_POST["step"];
$zOnly = $_POST["z_only"];




$Gp_list = (array) null;
$Rp_list = (array) null;
$Cp_list = (array) null;
$Cs_list = (array) null;
$Z_list = (array) null;
$Phi_list = (array) null;
$F_list_Parallel = (array) null;
$F_list_Consistent = (array) null;

      //1) запрос -  вызываем функцию set_default
       //----------------------------------------------------send get request start single

        $urlGet = 'http://192.168.253.99:3456/setDefault';
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $urlGet);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $response = curl_exec($ch);
        curl_close($ch);
        if ($response == "false"){
            $_SESSION['err'] = 'Нет соединение с устройством';
            header("Location: ../view_object_page.php");
        }{
     //------------------------------------------------------send get request end  single

       //-----------------------------------CALL_ALL-------------------------------------------
       if(isset($zOnly)){
        //1)call func -  change_scheme
        $urlGet = 'http://192.168.253.99:3456/scheme';
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $urlGet);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $response = curl_exec($ch);
        //var_dump('get request result scheme:',$response);
        curl_close($ch);
        //2) main logic
        //Поочередно передаем частоту, шаг , z_only и  частоту в бинарном виде
        // muliple example request on arduino , use curl START

        for ($i = $f_Start; $i < $f_End + $step; $i+=$step) {
            //_________START SET_FREQ___
            $ch = curl_init();
            // Set the URL and other options
            $urlPost = 'http://192.168.253.99:3456/setFreq';
            curl_setopt($ch, CURLOPT_URL, $urlPost);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $i);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            // Make the request
            $response = curl_exec($ch);
            var_dump('post request result set_freq:',$response);
            // Close the cURL session
            curl_close($ch);
    //END SET_FREQ___

                $ch = curl_init();
                // Set the URL and other options
                $urlPost = 'http://192.168.253.99:3456/calcAll';
                curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
                curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                // Make the request наш массив данных
                $response = curl_exec($ch);

                // Close the cURL session
                curl_close($ch);

                //ДОПИСАТЬ МАТЕМАТИКУ response это JSON его нужно преобразовать в массив


                $pi = pi();
 
                if ($f != 0 && $z != 0 && $fi != 0 ){
                array_push($F_list_Parallel,($i/1000.0));
                array_push($Gp_list,(cos($fi) / abs($z)));
                array_push($Rp_list,(abs($z) / cos($fi)));
                array_push($Cp_list,(1 / (2.0 * $pi * $f * abs($z) * sin(-$fi))));
                }
            }
            // muliple example request on arduino , use curl END
            //4)call func -  change_scheme
            $urlGet = 'http://192.168.253.99:3456/scheme';
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, $urlGet);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            $response = curl_exec($ch);
            //var_dump('get request result scheme:',$response);
            curl_close($ch);
        }

        //ЕСЛИ УСЛОВИЕ в IF не было выполнено 
        for ($i = $f_Start; $i < $f_End + $step; $i+=$step) {
            //_______________________CALL SET_FREQ START
            
            $ch = curl_init();
            // Set the URL and other options
            $urlPost = 'http://192.168.253.99:3456/setFreq';
            curl_setopt($ch, CURLOPT_URL, $urlPost);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $i);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            // Make the request
            $response = curl_exec($ch);
            var_dump('post request result set_freq:',$response);
            // Close the cURL session
            curl_close($ch);
            //_______________________CALL SET_FREQ end
            
            $ch = curl_init();
            // Set the URL and other options
            $urlPost = 'http://192.168.253.99:3456/calcAll';
            curl_setopt($ch, CURLOPT_URL, $urlGet);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            // Make the request
            $response = curl_exec($ch);
            var_dump('post request result ZOnly:',$response);
            // Close the cURL session
            curl_close($ch);
            
            //ДОПИСАТЬ МАТЕМАТИКУ response это JSON его нужно преобразовать в массив

            $pi = pi();
            if ($f != 0 && $z != 0 && $fi != 0 ){
            array_push($F_list_Consistent,($i/1000.0));
            array_push($Z_list,($z));
            array_push($Phi_list,($fi));
            }

        }
    //vendor data
    $date = date("Y-m-d");
    if (isset($zOnly)){
         foreach($Z_list as $i=>$z){
            #преобразования комплексного числа
            (string) $complexNumber = preg_replace('/[ij]/', '',(string) $complexNumber);

            (string) $parts = preg_split('/[-+]/', $complexNumber);

            $realPart = (float) $parts[0];
            $imaginaryPart = (float) $parts[1];

            $freq = $F_list_Consistent[$i];
            $phi = $Phi_list[$i];

            #добавление в базу данных
            mysqli_query($link,"INSERT INTO `parameters` (`Freq`,`z_real_path_parameters`,`z_imaginary_part_parameters`,`phi_parameters`,`measurement_date`,`objects_idobjects`)
                                VALUES()'$freq','$realPart','$imaginaryPart','$phi','$date','$id_object'");

         }
    }else{
        #преобразования комплексного числа
        (string) $complexNumber = preg_replace('/[ij]/', '',(string) $complexNumber);

        (string) $parts = preg_split('/[-+]/', $complexNumber);

        $realPart = (float) $parts[0];
        $imaginaryPart = (float) $parts[1];

        $freq = $F_list_Parallel[$i];
        $phi = $Phi_list[$i];
        $gp = $Gp_list[$i];
        $rp = $Rp_list[$i];
        $cp = $Cp_list[$i];

        #добавление в базу данных
        mysqli_query($link,"INSERT INTO`parameters` (`Freq`,`z_real_path_parameters`,`z_imaginary_part_parameters`,`phi_parameters`,`gp_parameters`,`rp_parameters`,`cp_parameters`,`measurement_date`,`objects_idobjects`)
                            VALUES()'$freq','$realPart','$imaginaryPart','$phi','$gp','$rp','$cp','$date','$id_object'");
    }
    $_SESSION['sucs'] = "Вычисления завершены и добавлены в базу";
    header("Location: ../view_object_page.php");
    }
        
?>
