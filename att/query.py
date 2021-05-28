from datetime import date
import datetime
import cx_Oracle
from connection import mvintegra
import connection


# from connection import (mvintegra)

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
    return list_agenda_cirurgica


def receiver_agenda():
    list_agenda = view_bloco()

    nlin = len(list_agenda)
    list_em_cirurgia = []
    list_aviso_cirurgico = []
    list_chamada_cirurgia = []
    list_em_recuperacao = []
    for i in range(0, nlin):

        if list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i]['prestador_cirurgia']:  # verificar
            aviso_cirurgico = list()
            aviso_cirurgico.append(list_agenda[i]['data_do_aviso'])
            aviso_cirurgico.append(list_agenda[i]['nome_paciente'])
            aviso_cirurgico.append(list_agenda[i]['prestador_cirurgia'])
            
            list_aviso_cirurgico.append(aviso_cirurgico)

        if list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i][
            'prestador_cirurgia'] and list_agenda[i]['dt_centro_cirurgico'] :
            em_cirurgia = list()
            em_cirurgia.append(list_agenda[i]['data_do_aviso'])
            em_cirurgia.append(list_agenda[i]['nome_paciente'])
            em_cirurgia.append(list_agenda[i]['prestador_cirurgia'])
            em_cirurgia.append(list_agenda[i]['dt_centro_cirurgico'])

            list_em_cirurgia.append(em_cirurgia)

        if list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i][
            'prestador_cirurgia'] and list_agenda[i]['dt_centro_cirurgico'] and list_agenda[i]['dt_chamada_transf']:
            chamada_cirurgia= list()
            chamada_cirurgia.append(list_agenda[i]['data_do_aviso'])
            chamada_cirurgia.append(list_agenda[i]['nome_paciente'])
            chamada_cirurgia.append(list_agenda[i]['prestador_cirurgia'])
            chamada_cirurgia.append(list_agenda[i]['dt_chamada_transf'])
            
            list_chamada_cirurgia.append(chamada_cirurgia)

        if list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and \
            list_agenda[i]['prestador_cirurgia']:
            em_recuperacao = list()
            em_recuperacao.append(list_agenda[i]['data_do_aviso'] )
            em_recuperacao.append(list_agenda[i]['nome_paciente'] )
            em_recuperacao.append(list_agenda[i]['prestador_cirurgia'] )
            em_recuperacao.append(list_agenda[i]['dt_entrada_rpa'] )
            em_recuperacao.append(list_agenda[i]['dt_saida_rpa'] )
            
            list_em_recuperacao.append(em_recuperacao)

        
    #end_for
    
    manda_gravar(list_aviso_cirurgico,list_em_cirurgia,list_chamada_cirurgia,list_em_recuperacao,list_agenda)


def grava_em_arquivo(nome_arquivo,nome_list,nlin ,ncol):

    with open(nome_arquivo, 'a') as arquivo:
        for perc in range(0,nlin):
            arquivo.write(str(nome_list[perc][ncol]) + '\n')
        # endfor
    # endwith


def manda_gravar(list_aviso_cirurgico,list_em_cirurgia,list_chamada_cirurgia,list_em_recuperacao,list_agenda):

    nlin_aviso_cir = len(list_aviso_cirurgico)
    ncol_aviso_cir = len(list_aviso_cirurgico[0])
    for i in range(0,ncol_aviso_cir):
        arquivo = ['list_aviso_cirurgico_data.txt','list_aviso_cirurgico_nome_pac.txt','list_aviso_cirurgico_prestador.txt']
        grava_em_arquivo(arquivo[i],list_aviso_cirurgico,nlin_aviso_cir,i)
    #endfor

    nlin_em_cir = len(list_em_cirurgia)
    ncol_em_cir = len(list_em_cirurgia[0])
    for i in range(0,ncol_em_cir):
        arquivo = ['list_em_cirurgia_data.txt','list_em_cirurgia_nome_pac.txt','list_em_cirurgia_prestador.txt','list_em_cirurgia_dt_entrada_centro_cir.txt']
        grava_em_arquivo(arquivo[i],list_em_cirurgia,nlin_em_cir,i)
    #endfor

    nlin_chamada_cir = len(list_chamada_cirurgia)
    ncol_chamada_cir = len(list_chamada_cirurgia[0])
    for i in range(0,ncol_chamada_cir):
        arquivo = ['list_chamada_cirurgia_data.txt','list_chamada_cirurgia_nome_pac.txt','list_chamada_cirurgia_prestador.txt','list_chamada_transf.txt']
        grava_em_arquivo(arquivo[i],list_chamada_cirurgia,nlin_chamada_cir,i)
    #endfor

    nlin_em_rec = len(list_em_recuperacao)
    ncol_em_rec = len(list_em_recuperacao[0])
    for i in range(0,ncol_em_rec):
        arquivo = ['list_em_recuperacao_data.txt','list_em_recuperacao_nome_pac.txt','list_em_recuperacao_prestador.txt','list_em_recuperacao_dt_entrada_rpa.txt','list_em_recuperacao_dt_saida_rpa.txt']
        grava_em_arquivo(arquivo[i],list_em_recuperacao,nlin_em_rec,i)
    #endfor   
   

receiver_agenda()
