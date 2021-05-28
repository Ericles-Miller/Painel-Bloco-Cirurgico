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
       }

       else if ($arq == 'list_chamada_cirurgia_data.txt' || $arq == 'list_chamada_cirurgia_dt_centro_cir.txt' || $arq == 'list_chamada_cirurgia_nome_pac.txt' || $arq == 'list_chamada_cirurgia_prestador.txt')
       {
            $id_list = 2;

            if     ($arq == 'list_chamada_cirurgia_data.txt')          $poss =1;
            else if($arq == 'list_chamada_cirurgia_nome_pac.txt')      $poss =3;
            else if($arq == 'list_chamada_cirurgia_dt_centro_cir.txt') $poss =2;
            else $poss = 4;
       }

        else if ($arq == 'list_em_cirurgia_data.txt' || $arq == 'list_em_cirurgia_dt_entrada_rpa.txt' || $arq == 'list_em_cirurgia_nome_pac.txt' || $arq == 'list_em_cirurgia_prestador.txt'|| $arq == 'list_em_recuperacao_data.txt')
        {
           $id_list = 3;

            if     ($arq == 'list_em_cirurgia_data.txt')           $poss =1;
            else if($arq == 'list_em_cirurgia_dt_entrada_rpa.txt') $poss =2;
            else if($arq == 'list_em_cirurgia_nome_pac.txt')       $poss =3;
            else if($arq == 'list_em_cirurgia_prestador.txt')      $poss =4;
            else $poss = 5;
        }

        else if ($arq == 'list_em_recuperacao_data.txt' || $arq == 'list_em_recuperacao_dt_centro_cir.txt' || $arq == 'list_em_recuperacao_dt_chamada_transf.txt' || $arq == 'list_em_recuperacao_dt_entrada_rpa.txt' || $arq == 'list_em_recuperacao_dt_saida_rpa.txt'|| $arq == 'list_em_recuperacao_nome_pac.txt' || $arq == 'list_em_recuperacao_prestador.txt')
        {
            $id_list = 4;

            if     ($arq == 'list_em_recuperacao_dt_centro_cir.txt')     $poss =1;
            else if($arq == 'list_em_recuperacao_dt_chamada_transf.txt') $poss =2;
            else if($arq == 'list_em_recuperacao_dt_entrada_rpa.txt')    $poss =3;
            else if($arq == 'list_em_recuperacao_dt_saida_rpa.txt')      $poss =4;
            else if($arq == 'list_em_recuperacao_nome_pac.txt')          $poss =5;
            else if($arq == 'list_em_recuperacao_data.txt')              $poss =7;
            else $poss = 6;
        }

        $size_arq = filesize($arq);
       
        $arq_open =fopen($arq, 'r');
        $list_name = array();
        
        while(!feof($arq_open)):
            $line = fgets($arq_open,$size_arq);
            array_push($list_name,$line);
        endwhile;
        
        fclose($arq_open);
        return array ($id_list, $poss, $list_name);

    }

   

    function receiver_data($arq_list) //vou receber os array com os nomes dos arquivos e a lista com as funcoes  vindo com a funcao abaixo dessa
    {
        $sizeArq = count($arq_list);
        echo $sizeArq."<br>";
        $list_chamada_cirurgia = array(array());
        $list_aviso_cirurgico  = array(array());
        $list_em_cirurgia      = array(array());
        $list_em_recuperacao   = array(array());

        for ($i=0; $i<= $sizeArq; $i++)
        {   
            list($id,$ncol,$vet_receiver) = print_data($arq_list[$i]); 
            if ($id == 1)
            {   
                if ($ncol == 1)
                {   echo $i."<br>";
                    echo $vet_receiver[$i]."<br>";
                    $list_aviso_cirurgico['data'][$i] = $vet_receiver;
                }
                if($ncol == 2)
                {
                    $list_aviso_cirurgico['nome_pac'][$i] = $vet_receiver;
                }
                if ($ncol == 3)
                {
                    $list_aviso_cirurgico['prestador'][$i] = $vet_receiver;
                }
            }
            
            if($id == 2)
            {
                $list_chamada_cirurgia[$i][$ncol] = $vet_receiver;
                
            }
            if($id == 3)
            {
                $list_em_cirurgia[$i][$ncol] =$vet_receiver;
            }
            if($id == 4)
            {
                $list_em_recuperacao[$i][$ncol] = $vet_receiver;
            }
        }

        return array ($list_aviso_cirurgico,$list_chamada_cirurgia,$list_em_cirurgia,$list_em_recuperacao);


       
    }

    function list_names()
    {   
        #$lista_dados = array();
        $nomes_arq = array (
            'list_aviso_cirurgico_data.txt','list_aviso_cirurgico_nome_pac.txt','list_aviso_cirurgico_prestador.txt',
            'list_chamada_cirurgia_data.txt','list_chamada_cirurgia_dt_centro_cir.txt','list_chamada_cirurgia_nome_pac.txt','list_chamada_cirurgia_prestador.txt',
            'list_em_cirurgia_data.txt','list_em_cirurgia_dt_entrada_rpa.txt','list_em_cirurgia_nome_pac.txt','list_em_cirurgia_prestador.txt','list_em_recuperacao_data.txt',
            'list_em_recuperacao_dt_centro_cir.txt','list_em_recuperacao_dt_chamada_transf.txt','list_em_recuperacao_dt_entrada_rpa.txt','list_em_recuperacao_dt_saida_rpa.txt','list_em_recuperacao_nome_pac.txt','list_em_recuperacao_prestador.txt'
        );

        
        list ($list_aviso_cirurgico,$list_chamada_cirurgia,$list_em_cirurgia,$list_em_recuperacao) = receiver_data($nomes_arq);

        //print_r($list_aviso_cirurgico);
        //echo($list_aviso_cirurgico[0][0]);
        echo('---------------------------------');
        //print_r($list_chamada_cirurgia);
        echo('---------------------------------');
        //print_r($list_em_cirurgia);
        echo('---------------------------------');
        //print_r($list_em_recuperacao);

    }

list_names();
?>
