<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css_index.css">
    <title>Bloco Cirúrgico</title>
</head>
<body>
    <div class="cabecalho_esquerdo" >
        <img src="./render/bitmap.png">
        <?php while ($dado = conn->fetch_array()){ ?>
        <table border="aviso_cirurgico">
            <tr>
                <td><?php echo $dado ["data_do_aviso"];?></td>    
                <td><?php echo $dado ["nome_paciente"];?></td>
                <td><?php echo $dado ["prestador_cirurgia"];?></td>
            </tr>
        </table>
        <?php}?>
    </div>

    <div class="cabecalho_direito">
        <img src="./render/em cirurgia.png" alt="">
        <?php while ($dado = conn->fetch_array()){ ?>
        <table border ="em_cirurgia">
            <tr>
                <td><?php echo $dado ["data_do_aviso"];?></td>
                <td><?php echo $dado ["nome_paciente"];?></td>
                <td><?php echo $dado ["prestador_cirurgia"];?></td>
                <td><?php echo $dado["dt_centro_cirurgico"];?></td> 
                <td><?php echo $dado["dt_centro_cirurgico"];?></td>
            </tr>    
        </table>
        <?php}?>
    </div>
    
    <div class="cabecalho_direito_2">
        <?php while ($dado = conn->fetch_array()){ ?>
        <img src="./render/em recuperacao.png" alt="">
        <table border = "em_recuperacao">
            <tr>
                <td><?php echo $dado["data_do_aviso"];?></td<td/td>
                <td><?php echo $dado["nome_paciente"];?></td>
                <td><?php echo $dado["prestador_cirurgia"];?><td>
                <td><?php echo $dado["dt_chamada_trasf"];?></td>
                <td><?php echo $dado["dt_centro_cirurgico"];?></td>
                <td><?php echo $dado["dt_entrada_rpa"];?></td>
                <td><?php echo $dado["dt_saida_rpa"];?></td>
            </tr>
        </table>
        <?php}?>
    </div>

    <div class="cabecalho_esquerdo_2">
        <?php while ($dado = conn->fetch_array()){ ?>
        <img src="./render/pagina bloco cirurgico.png" alt="">
        <table border= "chamada_cirugia">
            <tr>
                <td><?php echo $dado ["data_do_aviso"];?></td</t</td>
                <td><?php echo $dado ["nome_paciente"];?></td</t/td>
                <td><?php echo $dado ["prestador_cirurgia"];?></td>
                <td><?php echo $dado["dt_centro_cirurgico"];?></td>
            </tr>
        </table>
        <?php}?>
    </div>
</body>
</html>