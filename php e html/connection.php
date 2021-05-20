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
            $servidor = "10 .10.1.200 ";
            $user = "mvintegra";
            $pass = "dbamv";
            $dbname = "mvintegra"; #verificar o nome do banco 
            

            try
            {
                self::$con = new PDO("oracle:host=$servidor; dbname=$dbname;", $user, $pass);
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
?>













?>