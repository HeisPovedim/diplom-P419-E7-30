<?php

namespace App\Http\Controllers;

use App\Models\E7;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;
use Symfony\Component\String\ByteString;

class E7Controller extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function main(){
        return(view('welcome'));  
  }

  public function start(Request $request){
      dump('попал в контроллер');
      dump('z_only: ',$request->input('z_only'));

      $Gp_list = (array) null;
      $Rp_list = (array) null;
      $Cp_list = (array) null;
      $Cs_list = (array) null;
      $Z_list = (array) null;
      $Phi_list = (array) null;
      $F_list_Parallel = (array) null;
      $F_list_Consistent = (array) null;

      $f_Start = (int)$request->input('f_start');
      $f_End = (int)$request->input('f_end');
      $step = (int)$request->input('step');

      //1) запрос -  вызываем функцию set_default
       //----------------------------------------------------send get request start single

        $urlGet = 'http://192.168.253.99:3456/setDefault';
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $urlGet);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $response = curl_exec($ch);
       // dump('get request result set_default:',$response);
        curl_close($ch);
        //------------------------------------------------------send get request end  single

       //-----------------------------------CALL_ALL-------------------------------------------
        if(!$request->input('z_only')){
            //1)call func -  change_scheme
            $urlGet = 'http://192.168.253.99:3456/scheme';
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, $urlGet);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            $response = curl_exec($ch);
            //dump('get request result scheme:',$response);
            curl_close($ch);
        //2) main logic
        //Поочередно передаем частоту, шаг , z_only и  частоту в бинарном виде
        // muliple example request on arduino , use curl START

        for ($i = $f_Start; $i < $f_End + $step; $i+=$step) {
            //_________START SET_FREQ___
            $binary_f = pack("N", $i);
            $ch = curl_init();
            // Set the URL and other options
            $urlPost = 'http://192.168.253.99:3456/setFreq';
            curl_setopt($ch, CURLOPT_URL, $urlPost);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $binary_f);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            // Make the request
            $response = curl_exec($ch);
            dump('post request result set_freq:',$response);
            // Close the cURL session
            curl_close($ch);
       //END SET_FREQ___
            $data =[
                "f_start" => $i
            ];

                $ch = curl_init();
                // Set the URL and other options
                $urlPost = 'http://192.168.253.99:3456/calcAll';
                curl_setopt($ch, CURLOPT_URL, $urlPost);
                curl_setopt($ch, CURLOPT_POST, true);
                curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
                curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                // Make the request
                $response = curl_exec($ch); #какой тип изначально ?

                // Close the cURL session
                curl_close($ch);

                 //logic, operation data----------------
                 dd($response);
                $unpackData = unpack('>3B3bhiff', $response);

                $pacDataResult = explode(' ', $unpackData);
                dump($pacDataResult);
                $f = $pacDataResult[0];
                $z = $pacDataResult[1];
                $fi = $pacDataResult[2];
                $pi = pi();
                //dd($tmp);
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
            //dump('get request result scheme:',$response);
            curl_close($ch);
        }

        //ЕСЛИ УСЛОВИЕ в IF не было выполнено 
        for ($i = $f_Start; $i < $f_End + $step; $i+=$step) {
            //_______________________CALL SET_FREQ START
            
            $binary_f = pack("N", $i);
            $ch = curl_init();
            // Set the URL and other options
            $urlPost = 'http://192.168.253.99:3456/setFreq';
            curl_setopt($ch, CURLOPT_URL, $urlPost);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $binary_f);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            // Make the request
            $response = curl_exec($ch);
            dump('post request result set_freq:',$response);
            // Close the cURL session
            curl_close($ch);
            //_______________________CALL SET_FREQ end
            //$binary_f = pack("N", $F_Start);

            $data =[
                "f_start" => $i
            ];
            
            $ch = curl_init();
            // Set the URL and other options
            $urlPost = 'http://192.168.253.99:3456/calcAll';
            curl_setopt($ch, CURLOPT_URL, $urlPost);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

            // Make the request
            $response = curl_exec($ch);
            dump('post request result ZOnly:',$response);
            // Close the cURL session
            curl_close($ch);
            
             //logic, operation data----------------
            $tmp = explode(' ', $response);
            $f = $tmp[0];
            $z = (int)$tmp[1];
            $fi = (int)$tmp[2];
            $pi = pi();
            if ($f != 0 && $z != 0 && $fi != 0 ){
            array_push($F_list_Consistent,($i/1000.0));
            array_push($Z_list,($z));
            array_push($Phi_list,($fi));
            }

        }
        //------------------------------------------------------ muliple example request on arduino , use curl END 
        dump('-----------------------------------------------------------------------------');
        dump('post request result NotZOnly FREQ:',$i);
        dump($F_list_Parallel);
        dump($Gp_list);
        dump($Rp_list);
        dump($Cp_list);
        dump('post request result ZOnly FREQ:',$i);
        dump($F_list_Consistent);
        dump($Z_list);
        dump($Phi_list);
        
            
    }

    

}