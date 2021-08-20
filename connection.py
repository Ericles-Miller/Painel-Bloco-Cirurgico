import cx_Oracle


#conexão banco mvintegra
def mvintegra():
    dsn = cx_Oracle.makedsn (
        '',  #endereco e porta (retirei por motivos de segurança
        '' , 
        service_name ='prdmv'
    )
    conn = cx_Oracle.connect(
        user  =  '' , #retirei por motivos de segurança 
        password  =  '' ,
        dsn  =  dsn
    )
    return  conn  
    
