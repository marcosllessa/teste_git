import cx_Oracle

## DADOS DA CONEXÃO

ipaddress='localhost'
username='sys'
password='oracle'
port='1521'
tnsname='XEPDB1'

def conexao():
    return cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)



def close():

    connection.close()