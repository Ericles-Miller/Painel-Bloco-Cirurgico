from datetime import datetime, timedelta
import datetime # manipulacao de datas 
import os # converter data em string
import cx_Oracle #
from connection import mvintegra
import connection
import json # criar arquivo texto json
import time 
from operator import itemgetter  # ordenar dados de acordo com a data e hora 

def view_bloco():
    list_agenda_cirurgica = []
    connection = mvintegra()
    cursor = connection.cursor()
    #cursor_secundario = connection.cursor()

    # current_date = datetime.datetime.now()
    # date = current_date - datetime.timedelta(days = days)
    # date = date.strftime("%d/%m/%y")

    cont = 0
    select_requests = "select data_do_aviso, nome_paciente, prestador_da_cirurgia,dt_chamada_transf, dt_centro_cirurgico,data_da_cirurgia,dt_entrada_rpa,dt_saida_rpa,centro_Cirurgico from dbamv.vdic_agenda_cirurgia WHERE DT_AVISO >= to_date(SYSDATE) AND DT_AVISO < to_date(SYSDATE+1) AND CENTRO_CIRURGICO = 'ENDOSCOPIA'"
    request = cursor.execute(select_requests)
    for requests in cursor.execute(select_requests):
        view_agenda_cirurgica = {'data_do_aviso': requests[0], 'nome_paciente': requests[1],'prestador_cirurgia': requests[2], 'dt_chamada_transf': requests[3],'dt_centro_cirurgico': requests[4], 'data_da_cirurgia': requests[5],'dt_entrada_rpa': requests[6], 'dt_saida_rpa': requests[6],'centro_cirurgico': requests[7]}
        list_agenda_cirurgica.append(view_agenda_cirurgica)
        # end
    connection.commit()
    return list_agenda_cirurgica
    
       
def receiver_agenda_end():
    
    list_agenda = view_bloco()
    nlin = len(list_agenda)
    if list_agenda:
        for i in range(0,nlin):
            if list_agenda[i]['data_da_cirurgia'] is None:
                list_agenda[i]['data_da_cirurgia'] = 'vazio'
            
            #convet for string data and datetime
            if  list_agenda[i]['dt_chamada_transf'] is None:
                list_agenda[i]['dt_chamada_transf'] = 'vazio'
            else:
            #converter esse dado para string 
                aux = list_agenda[i]['dt_chamada_transf'].strftime('%d/%m/%Y %H:%M')
                list_agenda[i]['dt_chamada_transf'] = aux
            
            if  list_agenda[i]['dt_entrada_rpa'] is None: 
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
                aux = list_agenda[i]['centro_cirurgico'].strftime('%d/%m/%Y %H:%M:%S')
                list_agenda[i]['centro_cirurgico'] = aux
                
            if  list_agenda[i]['dt_saida_rpa'] is None: 
                list_agenda[i]['dt_saida_rpa'] = 'vazio'    
            else:             
                aux = list_agenda[i]['dt_saida_rpa'].strftime('%d/%m/%Y %H:%M')
                list_agenda[i]['dt_saida_rpa'] = aux  
                
        #end for
        
                
    
        nlin = len(list_agenda)
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
                

                if list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i]['prestador_cirurgia']and list_agenda[i]['dt_centro_cirurgico'] == 'vazio':
                    status = 'Aviso Cirúrgico'
                    dict_agenda['status'] = status
                '''
                if list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i]['prestador_cirurgia'] and list_agenda[i]['dt_centro_cirurgico'] != 'vazio' and list_agenda[i]['dt_chamada_transf'] == 'vazio':  # verificar
                    status = 'Chamada Cirurgica'
                    dict_agenda['status'] = status'''

                if  list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i]['prestador_cirurgia'] and list_agenda[i]['dt_chamada_transf'] != 'vazio' and list_agenda[i][
                'dt_entrada_rpa'] == 'vazio' and list_agenda[i]['dt_saida_rpa'] == 'vazio':  # verificar
                    status = 'Em Cirurgia'
                    dict_agenda['status'] = status
                
                if  list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i]['prestador_cirurgia'] and list_agenda[i][
                'dt_entrada_rpa'] != 'vazio' and list_agenda[i]['dt_saida_rpa'] == 'vazio' :  # verificar
                    status = 'Em Recuperação'
                    dict_agenda['status'] = status

                if list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i]['prestador_cirurgia'] and list_agenda[i][
                'dt_entrada_rpa'] != 'vazio' and list_agenda[i]['dt_saida_rpa'] != 'vazio':
                    status = 'Alta Bloco Cirúrgico'
                    dict_agenda['status'] = status
                    
                list_agenda_cirurgica.append(dict_agenda)
            #end if
        #endfor

        #funcao responsavel para ordenar os dados atraves da data
        list_agenda_cirurgica = sorted(list_agenda_cirurgica, key=itemgetter('data_aviso'))
        manda_gravar(list_agenda_cirurgica)
    
    else:
        print("Lista endoscopia vazia. O script fará uma nova pesquisa depois de 3 minutos.")
         

def manda_gravar(list_agenda_cirurgica):
    print(list_agenda_cirurgica)
    arquivo = 'list_agenda_endoscopia.json'
    grava_em_arquivo(arquivo,list_agenda_cirurgica)
    
def grava_em_arquivo(nome_arq,lista):
    with open(nome_arq, 'w', encoding='utf8') as f:
        json.dump(lista,f,ensure_ascii=False,sort_keys=True ,indent=4, separators=(',', ':'))
#end


