import connection
import os

import json
import csv
from cgs1 import CGS1
import pandas as pd
import schedule
import time
from datetime import datetime


ARQUIVO = 'busca_gtins'
path = 'C:/Troca/gtin/python/eanGS1/'
path_error = 'C:/Troca/gtin/python/error_eanGS1/'
df_ean = pd.read_csv(ARQUIVO + '.csv', sep=',')
df_ret2 = []
df_ret3 = []


def ret_gs1():
    try:
        for i in range(len(df_ean)):
            gtin = str(int(df_ean.iloc[i])).zfill(14)
            print(gtin)

            conect = CGS1()
            rest = conect.get_gtin(gtin)
            val = rest.json()
            try:

                if 'status' in val:
                    status = val['status']
                    print(status)
                    if status == 'Inválido':

                        with open(path_error + 'erro_' + gtin + '.json', 'w', newline='') as j:
                            json.dump(val, j)
                        df_ret3.append(gtin)

                    else:
                        df_ret2.append(gtin)

                        with open(path + gtin + '.json', 'w', newline='') as j:
                            json.dump(val, j)

            except:
                print('Ocorreu um erro na conexão com a API...')
                print('Gravando  dados para serem apagados da tabela de contigencia...')
                with open('RES_Cont_' + ARQUIVO + '.csv', 'w', newline='') as f:
                    gtin = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    for i in df_ret2:
                        gtin.writerow([i])
                with open('err_RES_Cont_' + ARQUIVO + '.csv', 'w', newline='') as f:
                    gtin = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    for i in df_ret3:
                        gtin.writerow([i])


        print("Fim da consulta")
    except:
        print('Erro na API')
        print('Ocorreu um erro na conexão com a API...')
        print('Gravando  dados para serem apagados da tabela de contigencia...')
        with open('RES_Cont_' + ARQUIVO + '.csv', 'w', newline='') as f:
            gtin = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in df_ret2:
                gtin.writerow([i])
        with open('err_RES_Cont_' + ARQUIVO + '.csv', 'w', newline='') as f:
            gtin = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in df_ret3:
                gtin.writerow([i])

def delete_cont(): #apaga o gtin da tabela de contigencia se já existe resultado da cosmos.

    import connection

    with open('RES_Cont_' + ARQUIVO + '.csv', newline='') as f:
        gtins = csv.reader(f, delimiter=';')

        for l in gtins:
            g = (str(', '.join(l)))
            #print(g)

            connect = connection.conexao()
            cursor = connect.cursor()  # cria um cursor
            cursor.execute("SELECT * from cont_gtin where gtin =" + g)  # consulta sql
            result = cursor.fetchone()
            if result == None:
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(now, 'O GTIN '+g+' não existe na tabela.')



            else:

                cursor.execute("delete from cont_gtin where gtin=" + g)  # consulta sql
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(now, 'GTIN '+g+' apagado da tabela de contigência')
                cursor.execute("commit")

    with open('err_RES_Cont_' + ARQUIVO + '.csv', newline='') as f:
        gtins = csv.reader(f, delimiter=';')

        for l in gtins:
            g = (str(', '.join(l)))

            connect = connection.conexao()
            cursor = connect.cursor()  # cria um cursor
            cursor.execute("SELECT * from cont_gtin where gtin =" + g)  # consulta sql
            result = cursor.fetchone()
            if result == None:
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(now, 'err...O GTIN ' + g + ' não existe na tabela.')



            else:

                cursor.execute("delete from cont_gtin where gtin=" + g)  # consulta sql
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(now, 'GTIN ' + g + ' apagado da tabela de contigência')
                cursor.execute("commit")




        with open('RES_Cont_' + ARQUIVO + '.csv', 'r+') as f:

            new_f = []
            new_f = f.readlines()
            f.seek(0)
            if new_f == []:
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(now, 'Scheduler_GS1  - Arquivos encontrados na busca na API: lista vazia')
            for l in range(len(new_f)):
                print('Imprimindo a lista...')
                print(g)
                if g not in new_f[l]:
                    print(new_f[l]+ ' gravado')
                    f.write(new_f[l])
                else:
                    print(new_f[l] + ' apagado')
            f.truncate()


        with open('err_RES_Cont_' + ARQUIVO + '.csv', 'r+') as f:

            new_f = []
            new_f = f.readlines()
            f.seek(0)
            if new_f == []:
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(now, 'Scheduler_GS1  - Arquivos encontrados na busca na API: lista vazia')
            for l in range(len(new_f)):
                print('Imprimindo a lista...')
                print(g)
                if g not in new_f[l]:
                    print(new_f[l]+ ' err...gravado')
                    f.write(new_f[l])
                else:
                    print(new_f[l] + ' err...apagado')
            f.truncate()

def scheduler_gs1():
    schedule.every(1800).seconds.do(ret_gs1)
    schedule.every(60).seconds.do(delete_cont)

    while True:

        schedule.run_pending()
        time.sleep(1)