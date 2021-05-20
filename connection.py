import cx_Oracle


#conexão banco mvintegra
def mvintegra():
    dsn = cx_Oracle.makedsn (
        '10.10.1.200',
        '1521' ,
        service_name ='prdmv'
    )
    conn = cx_Oracle.connect(
        user  =  'mvintegra' ,
        password  =  'dbamv' ,
        dsn  =  dsn
    )
    return  conn  
    