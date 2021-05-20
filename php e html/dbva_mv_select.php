<?php

//criar um obj pdo no padrão singleton 
class Conecta_Banco_mvintegra
{
    public static $con;
    public static Function conexao()
    {

        if (!isset(self::$con))
        {
            #CHAMANDO O BANCO DE DADOS 
            $servidor = "localhost";
            $user = "root";
            $pass = "adlo895020";
            $dbname = "mvintegra"; #verificar o nome do banco 
            

            try
            {
                self::$con = new PDO("mysql:host=$servidor; dbname=$dbname;", $user, $pass);
                self::$con->exec('SET CHARSET utf8');
            }
            catch(Exception $e)
            {
                echo $e->getMessage();
            }
        }
        return self::$con;
    }

}
$data_do_aviso;
$nome_paciente;
$prestador_cirurgia;
$dt_chamada_transf;
$dt_entrada_rpa;
$dt_saida_rpa;
$dt_centro_cirurgico; 
$centro_Cirurgico;


$select = "select data_do_aviso, nome_paciente, prestador_da_cirurgia,_dt_chamada_trasf, dt_centro_cirurgico,data_da_cirurgia,dt_entrada_rpa,dt_saida_rpa, centro_Cirurgico from vdic_agenda_cirurgia ";
$conn = $mysqli->query($select) or die($mysqli->error);













        /* #$aspas = '\';
            $colchete = ']';
            //cont = cont +1;
            $linha = fgets($arquivoAberto,$tamanhoArquivo);

            $a =strlen($linha);


            $sub = substr($linha, 2,16);
            array_push($aviso_cirurgico, $sub);

            for ($i= 0; $i<$a; $i++)
            {   
                if ($linha[$i] == ',')
                {
                    
                    $pos2 = $i+3;
                    
                }

                if ($linha[$i] == '\'')  //aspas simples salvando data
                {  
                    $pos1 = $i-1;
                    $sub = substr($linha,$pos1,$pos2);
                    array_push($aviso_cirurgico, $sub);
                }

                if ($linha[$i] == ',' && $linha[$i+1] == 'd')
                {
                    $pos_d = $i;
                    if ($linha[$i] == $colchete)
                    {
                        $pos_colc = $i-1;
                        $sub = substr($linha,$pos_d,$pos_colc);
                        array_push($aviso_cirurgico,$sub);
                    }
                }

                
            }*/


?>