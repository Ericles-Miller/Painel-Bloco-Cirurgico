let aviso_cir   = document.getElementById("aviso_cir")
let chamada_cir = document.getElementById("chamada_cir")
let em_cir      = document.getElementById("em_cir")
let em_rec      = document.getElementById("em_rec")
let cont = -1;
// window.location.reload()


    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
        var list_aviso_cir = JSON.parse(this.responseText); 
        document.getElementById("teste").innerHTML = `  
            <!-- Cabeçalho da tabela -->
            <tr class="active">
                <th>Paciente</th>
                <th>Data</th>
                <th>Prestador</th>
                <th>Chamada Transferência</th>
                <th>Status</th>
            </tr>
            ${data_aviso_cir()}
            </thead>
            <tbody>`
            function data_aviso_cir()
            {
                let list_aviso_cirurgico = list_aviso_cir; ///parei aqui
                let textTable = "";

                setInterval(() => {
                    cont++;
                    //if (cont == list_aviso_cirurgico.length - 1) cont = 0;
                    if (list_aviso_cirurgico[cont]['status'] == 'Alta Bloco Cirúrgico') {
                        alta_bloc.innerHTML = `
                            <h2>${list_aviso_cirurgico[cont]['nome_paciente']}</h3>
                            <h4> Recebeu alto do Bloco as ${list_aviso_cirurgico[cont]['data_aviso']}</h4>
                        `
                    }
                    if(list_aviso_cirurgico[cont]['status'] == 'Em Recuperação') {
                        em_rec.innerHTML =`
                        <h2>${list_aviso_cirurgico[cont]['nome_paciente']}</h3>
                        <h5>Entrada na Recuperação as ${list_aviso_cirurgico[cont]['dt_entrada_rpa']}</h5>`                   
                    
                    }
                    else if(list_aviso_cirurgico[cont]['status'] == 'Em Cirurgia')
                    {
                        em_cir.innerHTML =`
                        <h2>${list_aviso_cirurgico[cont]['nome_paciente']}</h3>
                        <h4>Em Cirurgia desde ${list_aviso_cirurgico[cont]['data_aviso']}</h4>`
                    }
                    else if(list_aviso_cirurgico[cont]['status']== 'Aviso Cirúrgico')
                    aviso_cir.innerHTML = `
                        <h2>${list_aviso_cirurgico[cont]['nome_paciente']}</h3>
                        <h4>Previsto para ${list_aviso_cirurgico[cont]['data_aviso']}</h4
                    ` 
                    
                }, 7000);//muda a cada 7 segundos

                for(let i in list_aviso_cir) {
                    textTable+= `
                    <tr>
                        <td>${list_aviso_cirurgico[i]['nome_paciente']}</td>
                        <td>	
                            <!-- class="hidden-xs" ->hidden-xs oculta a coluna em resoluções menores -->
                            <p>${list_aviso_cirurgico[i]['data_aviso']}</p>
                        </td>
                        <td>
                            <p>${list_aviso_cirurgico[i]['prestador_cirurgia']}</p>
                        </td>
                        <td>
                            <p>${list_aviso_cirurgico[i]['dt_chamada_transf']}
                        </td>
                        <td>
                            <p>${list_aviso_cirurgico[i]['status']}</p>
                        </td>
                    </tr>`

                }
                return textTable;
            }
        }

    };


xmlhttp.open("Post","list_agenda_cirurgica.json",true);
xmlhttp.send();

setInterval(()=>
{
window.location.reload(1)
},120000); //125 seg. atualiza o script*/

