<?php
function print_data($arq)
{   
    $list_name = array();

   if ($arq == 'list_aviso_cirurgico_data.txt' || $arq == 'list_aviso_cirurgico_nome_pac.txt' || $arq == 'list_aviso_cirurgico_prestador.txt')
   {    
       $id_list = 1;

       if     ($arq == 'list_aviso_cirurgico_data.txt')     $poss =1;
       else if($arq == 'list_aviso_cirurgico_nome_pac.txt') $poss =2;
       else $poss =3;
       echo $poss."<br>";
   }

   else if ($arq == 'list_chamada_cirurgia_data.txt' || $arq == 'list_chamada_transf.txt' || $arq == 'list_chamada_cirurgia_nome_pac.txt' || $arq == 'list_chamada_cirurgia_prestador.txt')
   {
        $id_list = 2;

        if     ($arq == 'list_chamada_cirurgia_data.txt')       $poss =1;
        else if($arq == 'list_chamada_cirurgia_nome_pac.txt')   $poss =3;
        else if($arq == 'list_chamada_transf.txt')              $poss =2;
        else $poss = 4;
        echo $poss."<br>";
   }

    else if ($arq == 'list_em_cirurgia_data.txt'  || $arq == 'list_em_cirurgia_nome_pac.txt' || $arq == 'list_em_cirurgia_prestador.txt'|| $arq == 'list_em_cirurgia_dt_entrada_centro_cir')
    {
       $id_list = 3;

        if     ($arq == 'list_em_cirurgia_data.txt')                  $poss =1;
        else if($arq == 'list_em_cirurgia_dt_entrada_centro_cir.txt') $poss =2;
        else if($arq == 'list_em_cirurgia_nome_pac.txt')              $poss =3;
        else if($arq == 'list_em_cirurgia_prestador.txt')             $poss =4;
        
        echo $poss."<br>";
    }

    else if ( $arq == 'list_em_recuperacao_data.txt' || $arq == 'list_em_recuperacao_dt_entrada_rpa.txt' || $arq == 'list_em_recuperacao_dt_saida_rpa.txt'|| $arq == 'list_em_recuperacao_nome_pac.txt' || $arq == 'list_em_recuperacao_prestador.txt')
    {
        $id_list = 4;
        
        if     ($arq == 'list_em_recuperacao_data.txt')              $poss =1; 
        else if($arq == 'list_em_recuperacao_dt_entrada_rpa.txt')    $poss =2;
        else if($arq == 'list_em_recuperacao_dt_saida_rpa.txt')      $poss =3;
        else if($arq == 'list_em_recuperacao_nome_pac.txt')          $poss =4;
        else $poss =5;

        echo $poss."<br>";
    }

    $size_arq = filesize($arq);
   
    $arq_open =fopen($arq, 'r');
    $list_name = array();
    
    while(!feof($arq_open)):
        $line = fgets($arq_open,$size_arq);
        array_push($list_name,$line);
    endwhile;
    
    fclose($arq_open);
    
    return array ($id_list, $poss,array_values($list_name));

}


function receiver_data($arq_list,$nlin) //vou receber os array com os nomes dos arquivos e a lista com as funcoes  vindo com a funcao abaixo dessa
    {
        
        //$sizeArq = count($arq_list);
        $list_chamada_cirurgia_data     = array();
        $list_chamada_cirurgia_nome_pac = array();
        $list_chamada_cirurgia_prestador= array();
        $list_chamada_dt_chamada_transf = array();

        $list_aviso_cirurgico_data      = array();
        $list_aviso_cirurgico_nome_pac  = array();
        $list_aviso_cirurgico_prestador = array();
        
        $list_em_cirurgia_data           = array();
        $list_em_cirurgia_nome_pac       = array();
        $list_em_cirurgia_prestador      = array();
        $list_em_cirurgia_dt_entrada_centro_cir = array();


        $list_em_recuperacao_data               = array();
        $list_em_recuperacao_nome_pac           = array();
        $list_em_recuperacao_prestador          = array();
        $list_em_recuperacao_dt_entrada_rpa     = array();
        $list_em_recuperacao_dt_saida_rpa       = array();

        for ($i=0; $i<$nlin; $i++)
        {   
            list($id,$ncol,$vet_receiver) = print_data($arq_list[$i]);
                        
            if ($id == 1)
            {   
                if ($ncol == 1) array_push($list_aviso_cirurgico_data, $vet_receiver);
                
                if($ncol  == 2) array_push($list_aviso_cirurgico_nome_pac,$vet_receiver);
                
                if ($ncol == 3) array_push($list_aviso_cirurgico_prestador,$vet_receiver);
            }

            if ($id == 2)
            {
                if($ncol == 1) array_push($list_chamada_cirurgia_data,$vet_receiver);
                    
                if($ncol == 3) array_push($list_chamada_cirurgia_nome_pac,$vet_receiver);
            
                if($ncol == 2) array_push($list_chamada_dt_chamada_transf,$vet_receiver);

                if($ncol == 4) array_push($list_chamada_cirurgia_prestador,$vet_receiver);

            }

            if ($id == 3)
            {
                if($ncol == 1) array_push($list_em_cirurgia_data,$vet_receiver);
                    
                if($ncol == 3) array_push($list_em_cirurgia_nome_pac,$vet_receiver);

                if($ncol == 4) array_push($list_em_cirurgia_prestador,$vet_receiver);
                    
                if($ncol == 2) array_push($list_em_cirurgia_dt_entrada_centro_cir,$vet_receiver);

            }

            if ($id == 4)
            {
                if($ncol == 1)array_push( $list_em_recuperacao_data,$vet_receiver);
                    
                if($ncol == 4)array_push( $list_em_recuperacao_nome_pac,$vet_receiver);
                
                if($ncol == 5)array_push( $list_em_recuperacao_prestador, $vet_receiver);
                    
                if($ncol == 2)array_push( $list_em_recuperacao_dt_entrada_rpa, $vet_receiver);

                if($ncol == 3)array_push( $list_em_recuperacao_dt_saida_rpa,$vet_receiver);
            }
        }
                

        return array(array_values($list_chamada_cirurgia_data),array_values($list_chamada_cirurgia_nome_pac),array_values($list_chamada_cirurgia_prestador),array_values($list_chamada_dt_chamada_transf),
        array_values($list_aviso_cirurgico_data),array_values($list_aviso_cirurgico_nome_pac),array_values($list_aviso_cirurgico_prestador),
        array_values($list_em_cirurgia_data),array_values($list_em_cirurgia_nome_pac),array_values($list_em_cirurgia_prestador),array_values($list_em_cirurgia_dt_entrada_centro_cir),
        array_values($list_em_recuperacao_data),array_values($list_em_recuperacao_nome_pac),array_values($list_em_recuperacao_prestador),
        array_values($list_em_recuperacao_dt_entrada_rpa),array_values($list_em_recuperacao_dt_saida_rpa));
    }

function list_names()
    {   
        #$lista_dados = array();
        $nomes_arq = array (
            'list_aviso_cirurgico_data.txt','list_aviso_cirurgico_nome_pac.txt','list_aviso_cirurgico_prestador.txt',
            'list_chamada_cirurgia_data.txt','list_chamada_transf.txt','list_chamada_cirurgia_nome_pac.txt','list_chamada_cirurgia_prestador.txt',
            'list_em_cirurgia_data.txt','list_em_cirurgia_nome_pac.txt','list_em_cirurgia_prestador.txt','list_em_cirurgia_dt_entrada_centro_cir.txt',
            'list_em_recuperacao_data.txt','list_em_recuperacao_dt_entrada_rpa.txt','list_em_recuperacao_dt_saida_rpa.txt','list_em_recuperacao_nome_pac.txt','list_em_recuperacao_prestador.txt'
        );

        $size_array = count($nomes_arq);
        
        echo $size_array;
        
        list ($list_chamada_cirurgia_data,$list_chamada_cirurgia_nome_pac,$list_chamada_cirurgia_prestador,$list_chamada_dt_chamada_transf,
        $list_aviso_cirurgico_data,$list_aviso_cirurgico_nome_pac,$list_aviso_cirurgico_prestador,
        $list_em_cirurgia_data,$list_em_cirurgia_nome_pac,$list_em_cirurgia_prestador,$list_em_cirurgia_dt_entrada_centro_cir,
        $list_em_recuperacao_data,$list_em_recuperacao_nome_pac,$list_em_recuperacao_prestador,$list_em_recuperacao_dt_entrada_rpa,
        $list_em_recuperacao_dt_saida_rpa) = receiver_data($nomes_arq,$size_array);

        echo "chamada cirurgia data <br>";
        print_r($list_chamada_cirurgia_data);
        echo("<br>---------------------------------<br>");
        echo "chamada cirurgia nome paciente <br>";
        print_r($list_chamada_cirurgia_nome_pac);
        echo("<br>---------------------------------<br>");
        echo "chamada cirurgia chamada data transferencia <br>";
        print_r($list_chamada_dt_chamada_transf);
        echo("<br>---------------------------------<br>");
        echo "chamada cirurgia prestador <br>";
        print_r($list_chamada_cirurgia_prestador);


        echo("<br><br>---------------------------------<br>");
        echo "aviso cirurgico data <br>";
        print_r($list_aviso_cirurgico_data);
        echo("<br>---------------------------------<br>");
        echo "aviso cirurgico nome paciente <br>";
        print_r($list_aviso_cirurgico_nome_pac);
        echo("<br>---------------------------------<br>");
        echo "<br>aviso cirurgico prestador <br>";
        print_r($list_aviso_cirurgico_prestador);

        echo("<br><br>---------------------------------<br>");
        echo "aviso em cirurgia data <br>";
        print_r($list_em_cirurgia_data);
        echo("<br>---------------------------------<br>");
        echo "<br>aviso em cirurgia nome paciente <br>";
        print_r($list_em_cirurgia_nome_pac);
        echo("<br>---------------------------------<br>");
        echo "<br>aviso em cirurgia prestador <br>";
        print_r($list_em_cirurgia_prestador);
        echo("<br>---------------------------------<br>");
        echo "<br>aviso em cirurgia data entrada centro cirurgico <br>";
        print_r($list_em_cirurgia_dt_entrada_centro_cir);


        echo("<br><br>---------------------------------<br>");
        echo " em recuperacao data <br>";
        print_r($list_em_recuperacao_data);
        echo("<br>---------------------------------<br>");
        echo "<br> em recuperacao nome do paciente <br>";
        print_r($list_em_recuperacao_nome_pac);
        echo("<br>---------------------------------<br>");
        echo "<br> em recuperacao prestador <br>";
        print_r($list_em_recuperacao_prestador);
        echo("<br>---------------------------------<br>");
        echo "<br> em recuperacao entrada recuperacao <br>";
        print_r($list_em_recuperacao_dt_entrada_rpa);
        echo("<br>---------------------------------<br>");
        echo "<br> em recuperacao data de saida <br>";
        print_r($list_em_recuperacao_dt_saida_rpa);
        
    }

function import_data($list_chamada_cirurgia_data,$list_chamada_cirurgia_nome_pac,$list_chamada_cirurgia_prestador,$list_chamada_dt_chamada_transf,
$list_aviso_cirurgico_data,$list_aviso_cirurgico_nome_pac,$list_aviso_cirurgico_prestador,
$list_em_cirurgia_data,$list_em_cirurgia_nome_pac,$list_em_cirurgia_prestador,$list_em_cirurgia_dt_entrada_centro_cir,
$list_em_recuperacao_data,$list_em_recuperacao_nome_pac,$list_em_recuperacao_prestador,$list_em_recuperacao_dt_entrada_rpa,
$list_em_recuperacao_dt_saida_rpa)
{
    
    for ($i = 0; $i<16; $i++)
    {
        $chamada_cirurgia_data      =$list_chamada_cirurgia_data[$i];
        $chamada_cirurgia_nome_pac  =$list_chamada_cirurgia_nome_pac[$i];
        $chamada_cirurgia_prestador =$list_chamada_cirurgia_prestador[$i];
        $chamada_dt_chamada_transf  =$list_chamada_dt_chamada_transf[$i];

        $aviso_cirurgico_data      =$list_aviso_cirurgico_data;
        $aviso_cirurgico_nome_pac  =$list_aviso_cirurgico_nome_pac;
        $aviso_cirurgico_prestador =$list_aviso_cirurgico_prestador;

        $cirurgia_data           = $list_em_cirurgia_data;
        $cirurgia_nome_pac       =$list_em_cirurgia_nome_pac;
        $cirurgia_prestador      =$list_em_cirurgia_prestador;
        $cirurgia_dt_entrada_centro_cir =$list_em_cirurgia_dt_entrada_centro_cir;

        $recuperacao_data               = $list_em_recuperacao_data;
        $recuperacao_nome_pac           = $list_em_recuperacao_nome_pac;
        $recuperacao_prestador          = $list_em_recuperacao_prestador;
        $recuperacao_dt_entrada_rpa     = $list_em_recuperacao_dt_entrada_rpa;
        $recuperacao_dt_saida_rpa       = $list_em_recuperacao_dt_saida_rpa;
    }
}











list_names();




