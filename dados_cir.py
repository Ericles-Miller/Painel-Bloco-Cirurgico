from datetime import date, datetime
import datetime
import cx_Oracle
from connection import mvintegra
import connection
import json
import time
from operator import itemgetter

def view_bloco():
    list_agenda_cirurgica = []
    connection = mvintegra()
    cursor = connection.cursor()
    cursor_secundario = connection.cursor()

    # current_date = datetime.datetime.now()
    # date = current_date - datetime.timedelta(days = days)
    # date = date.strftime("%d/%m/%y")

    cont = 0
    select_requests = "select data_do_aviso, nome_paciente, prestador_da_cirurgia,dt_chamada_transf, dt_centro_cirurgico,data_da_cirurgia,dt_entrada_rpa,dt_saida_rpa,centro_Cirurgico from dbamv.vdic_agenda_cirurgia WHERE DT_AVISO >= to_date(SYSDATE) AND DT_AVISO <= to_date(SYSDATE+1)"
    request = cursor.execute(select_requests)
    for requests in cursor.execute(select_requests):
        view_agenda_cirurgica = {'data_do_aviso': requests[0], 'nome_paciente': requests[1],'prestador_cirurgia': requests[2], 'dt_chamada_transf': requests[3],'dt_centro_cirurgico': requests[4], 'data_da_cirurgia': requests[5],'dt_entrada_rpa': requests[6], 'dt_saida_rpa': requests[6],'centro_cirurgico': requests[7]}
        list_agenda_cirurgica.append(view_agenda_cirurgica)
        # end
    connection.commit()

    if list_agenda_cirurgica:
        return list_agenda_cirurgica
    else:
        print("Lista bloco cirurgico vazia. O script fará uma nova pesquisa depois de 1 hora.")
        time.sleep(3600) #mudar para 1 hora 
        receiver_agenda()

def receiver_agenda():
    list_agenda = view_bloco()
    nlin = len(list_agenda)

    for i in range(0,nlin):
        #convet for strind data and datetime
        if  list_agenda[i]['dt_chamada_transf'] is None:
            list_agenda[i]['dt_chamada_transf'] = 'vazio'
        else:
          #converter esse dado para string 
            aux = list_agenda[i]['dt_chamada_transf'].strftime('%d/%m/%Y %H:%M')
            list_agenda[i]['dt_chamada_transf'] = aux

        if  list_agenda[i]['dt_saida_rpa'] is None: 
            list_agenda[i]['dt_saida_rpa'] = 'vazio'
        else:
           aux = list_agenda[i]['dt_saida_rpa'].strftime('%d/%m/%Y %H:%M')
           list_agenda[i]['dt_saida_rpa'] = aux

        if  list_agenda[i]['dt_entrada_rpa']is None: 
            list_agenda[i]['dt_entrada_rpa'] = 'vazio'
        else:
           aux = list_agenda[i]['dt_entrada_rpa'].strftime('%d/%m/%Y %H:%M')
           list_agenda[i]['dt_entrada_rpa'] = aux

        if  list_agenda[i]['dt_centro_cirurgico'] is None:
            list_agenda[i]['dt_centro_cirurgico'] = 'vazio'
        else:
            aux = list_agenda[i]['dt_centro_cirurgico'].strftime('%d/%m/%Y %H:%M')
            list_agenda[i]['dt_centro_cirurgico'] = aux
        
        if  list_agenda[i]['centro_cirurgico'] is None:
            list_agenda[i]['centro_cirurgico'] = 'vazio'
        else:
            aux = list_agenda[i]['centro_cirurgico'].strftime('%d/%m/%Y %H:%M')
            list_agenda[i]['centro_cirurgico'] = aux
    #end for
    
   

    list_agenda_cirurgica  = []
    for i in range(0, nlin):
        if list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i]['prestador_cirurgia'] and list_agenda[i][
            'dt_chamada_transf'] and list_agenda[i]['dt_centro_cirurgico'] and list_agenda[i]['data_da_cirurgia'] and list_agenda[i][
            'dt_entrada_rpa'] and list_agenda[i]['dt_saida_rpa'] and list_agenda[i]['centro_cirurgico']:
            
            dict_agenda = dict()
            dict_agenda['data_aviso']           = list_agenda[i]['data_do_aviso']
            dict_agenda['nome_paciente']        = list_agenda[i]['nome_paciente']
            dict_agenda['prestador_cirurgia']   = list_agenda[i]['prestador_cirurgia']
            dict_agenda['dt_chamada_transf']    = list_agenda[i]['dt_chamada_transf']
            dict_agenda['dt_centro_cirurgico']  = list_agenda[i]['dt_centro_cirurgico']
            dict_agenda['data_da_cirurgia']     = list_agenda[i]['data_da_cirurgia']
            dict_agenda['dt_entrada_rpa']       = list_agenda[i]['dt_entrada_rpa']
            dict_agenda['dt_saida_rpa']         = list_agenda[i]['dt_saida_rpa']
            dict_agenda['centro_cirurgico']     = list_agenda[i]['centro_cirurgico']
            

            if list_agenda[i]['data_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i]['prestador_cirurgia']:
                status = 'Aviso Cirúrgico'
                dict_agenda['status'] = status

            if list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i]['prestador_cirurgia'] and list_agenda[i]['dt_centro_cirurgico'] != 'vazio':  # verificar
                status = 'Em Cirurgia'
                dict_agenda['status'] = status

            if  list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i]['prestador_cirurgia'] and list_agenda[i]['dt_chamada_transf'] != 'vazio':  # verificar
                status = 'Chamada Cirurgia'
                dict_agenda['status'] = status
            
            if  list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i]['prestador_cirurgia'] and list_agenda[i][
            'dt_entrada_rpa'] != 'vazio' and list_agenda[i]['dt_saida_rpa'] != 'vazio':  # verificar
                status = 'Em Recuperação'
                dict_agenda['status'] = status

            list_agenda_cirurgica.append(dict_agenda)
        #end if
    #endfor

    #funcao responsavel para ordenar os dados atraves da data
    list_agenda_cirurgica = sorted(list_agenda_cirurgica, key=itemgetter('data_aviso'))
    teste = len(list_agenda_cirurgica)
    

    time.sleep(3800) #repete a execucao do script a cada 3 horas
    receiver_agenda()


def manda_gravar(list_agenda_cirurgica):
    
    arquivo = 'list_agenda_cirurgica.json'
    grava_em_arquivo(arquivo,list_agenda_cirurgica)
    
def grava_em_arquivo(nome_arq,lista):
    with open(nome_arq, 'w', encoding='utf8') as f:
        json.dump(lista,f,ensure_ascii=False,sort_keys=True ,indent=4, separators=(',', ':'))
#end

receiver_agenda()
