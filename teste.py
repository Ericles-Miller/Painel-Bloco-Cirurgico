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

    #lendo_arquivos(list_agenda_cirurgica)

    return list_agenda_cirurgica


def receiver_agenda():
    list_agenda = view_bloco()

    nlin = len(list_agenda)
    
    data_aviso_cirurgico     = list()
    nome_pac_aviso_cirurgico = list()
    prest_aviso_cirurgico    = list()
    ##########################################
    #em cirurgia
    data_aviso_em_cirurgia  = list()
    nome_pac_em_cirurgia    = list()
    prest_em_cirurgia       = list()
    dt_centro_em_cirurgia   = list()
#----------------chamado cirugia /----------------------------
    data_chamada_cirugia     = list()
    nome_pac_chamada_cirugia = list()
    prestador_chamada_cirugia= list()
    dt_centro_chamada_cirugia= list()
#-----------------------------em recuperacao
    data_em_recuperacao          = list()
    nome_pac_em_recuperacao      = list()
    prestador_em_recuperacao     = list()
    dt_centro_em_recuperacao     = list()
    dt_ch_tr_em_recuperacao      = list()
    dt_centro_cir_em_recuperacao = list()
    dt_entrada_em_recuperacao    = list()
    dt_saida_em_recuperacao      = list()

    for i in range(0, nlin):

        if list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i]['prestador_cirurgia']:  # verificar
            
            data_aviso_cirurgico.append(list_agenda[i]['data_do_aviso'])
            nome_pac_aviso_cirurgico.append(list_agenda[i]['nome_paciente'])
            prest_aviso_cirurgico.append(list_agenda[i]['prestador_cirurgia'])
            

        if list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i][
            'prestador_cirurgia'] and list_agenda[i]['dt_centro_cirurgico']:

            data_aviso_em_cirurgia.append(list_agenda[i]['data_do_aviso'])
            nome_pac_em_cirurgia.append(list_agenda[i]['nome_paciente'])
            prest_em_cirurgia.append(list_agenda[i]['prestador_cirurgia'])
            dt_centro_em_cirurgia.append(list_agenda[i]['dt_centro_cirurgico'])
            
        if list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i][
            'prestador_cirurgia'] and list_agenda[i]['dt_centro_cirurgico']:

            data_chamada_cirugia.append(list_agenda[i]['data_do_aviso'])
            nome_pac_chamada_cirugia.append(list_agenda[i]['nome_paciente'])
            prestador_chamada_cirugia.append(list_agenda[i]['prestador_cirurgia'])
            dt_centro_chamada_cirugia.append(list_agenda[i]['dt_centro_cirurgico'])
            

        if list_agenda[i]['data_do_aviso'] and list_agenda[i]['nome_paciente'] and list_agenda[i][
            'prestador_cirurgia'] and list_agenda[i]['dt_centro_cirurgico'] and list_agenda[i]['dt_chamada_transf'] and \
                list_agenda[i]['dt_centro_cirurgico'] and list_agenda[i]['dt_entrada_rpa'] and list_agenda[i][
            'dt_saida_rpa']:

            data_em_recuperacao.append(list_agenda[i]['data_do_aviso'] )
            nome_pac_em_recuperacao.append(list_agenda[i]['nome_paciente'] )
            prestador_em_recuperacao.append(list_agenda[i]['prestador_cirurgia'] )
            dt_centro_em_recuperacao.append(list_agenda[i]['dt_centro_cirurgico'] )
            dt_ch_tr_em_recuperacao.append(list_agenda[i]['dt_chamada_transf'] )
            dt_centro_cir_em_recuperacao.append(list_agenda[i]['dt_centro_cirurgico'])
            dt_entrada_em_recuperacao.append(list_agenda[i]['dt_entrada_rpa'] )
            dt_saida_em_recuperacao.append(list_agenda[i]['dt_saida_rpa'] )
            
    #end_for

    data_aviso_cirurgico     = list()
    data_em_recuperacao          = list()
    grava_em_arquivo(data_aviso_cirurgico,nome_pac_aviso_cirurgico,prest_aviso_cirurgico,data_aviso_em_cirurgia,nome_pac_em_cirurgia,prest_em_cirurgia,dt_centro_em_cirurgia,data_chamada_cirugia,nome_pac_chamada_cirugia,prestador_chamada_cirugia,dt_centro_chamada_cirugia,nome_pac_em_recuperacao,prestador_em_recuperacao
   
    
