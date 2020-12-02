import schedule
import time
from datetime import datetime
import json
import apiCosmos
import apiGs1

'''Ainda falta a integração com as informações que virão da SEFAZ(NFe). Como será o formato da informação de entrada?'''

def contigencia():


    import connection
    import csv

    connect = connection.conexao()

    cursor = connect.cursor()  # cria um cursor
    cursor.execute("SELECT * from cont_gtin")  # consulta sql
    result = cursor.fetchall()  # busca o resultado da consulta

    if result == None:
        print(now, "Nenhum Resultado")

    else:
        cont = []
        for i in range(len(result)):
            if result[i][1]>0:
                r = result[i][1]
                cont.append(r)

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now, cont)


    with open('busca_gtins.csv', 'w', newline='') as f:
        gtin = csv.writer(f, delimiter=';',
                          quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in cont:
            gtin.writerow([i])


def monitor_gtin():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    CONFIG = 'config_api'
    schedule.every(60).seconds.do(contigencia)
    print(now, 'Iniciando monitoramento da lista de GTINS...')


    try:
        with open(CONFIG + '.txt', 'r+') as f:

            conf = json.loads(f.read())
            print(now, 'Lendo arquivo de configuração...')
            print(now, conf)

            try:
                if 'api_1' in conf:
                    config1 = conf['api_1']
                if 'api_2' in conf:
                    config2 = conf['api_2']

                    if ('gs1' in config1 and 'cosmos' in config2):
                            print(now, 'Iniciando api gs1')
                            apiGs1.scheduler_gs1()
                            #apiCosmos.scheduler_cosmos()

                    if ('cosmos' in config1 and 'gs1' in config2):
                        print(now, 'Iniciando api cosmos')
                        apiCosmos.scheduler_cosmos()

                    else:
                        print(now, 'Parâmetros não configurados. Verifique o arquivo de configuração. API não iniciada.')
                        print(now, 'Iniciando monitoramento da lista de GTINS...')
            except:
                print(now, 'Error...Verifique o arquivo de Configuração de API')
                print(now, 'Iniciando monitoramento da lista de GTINS...')
    except:
        print(now, 'Erro...Verifique o arquivo de Configuração de API')
        print(now, 'Iniciando monitoramento da lista de GTINS...')

    while True:

        schedule.run_pending()
        time.sleep(1)

monitor_gtin()
