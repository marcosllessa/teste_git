import pandas as pd
import json
import urllib.request as url
from urllib.error import URLError, HTTPError
import csv
import schedule
import time
from datetime import datetime


ARQUIVO = 'busca_gtins'
#TOKEN = 'AJTUZtL-GRZ36F3RW2xpSg'
#TOKEN = '0iwjugcTcGRUL7ln31I1wg' #msn
TOKEN = 'bmyZTgnWrG_tM0Upndk2vQ'#BETH

df_ean = pd.read_csv(ARQUIVO + '.csv', sep=',')
headers = {
    'X-Cosmos-Token': TOKEN,
    'Content-Type': 'application/json'
}
endpoint = 'https://api.cosmos.bluesoft.com.br/gtins/'


def get_cosmos(endpoint,gtin,headers):

    req = url.Request(endpoint + gtin, None, headers)

    try:
        response = url.urlopen(req)
        print(response)
    except HTTPError as e:
        return [],e.code
    except URLError as e:
        return [],e.reason
    else:
        data = json.loads(response.read())

    return data,0


def ret_cosmos():
    path = 'C:/Troca/gtin/python/ean/'
    df_ret1 = []
    df_ret2 = []

    for i in range(len(df_ean)):
        gtin = str(int(df_ean.iloc[i])).zfill(14)
        data,e = get_cosmos(endpoint,gtin,headers)
        print(i,gtin,e)

        if(e==0):
            df_ret1 = data


            df_ret2.append(gtin)
            print('gtin:', gtin)

        if(len(df_ret1)>0):

            df_ret1 = data
            print(df_ret1)
            with open(path+gtin + '.json', 'w', newline='') as j:
                json.dump(df_ret1, j)

        if(len(df_ret2)>0):
            with open('RES_Cont_' + ARQUIVO + '.csv', 'w', newline='') as f:
                gtin = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for i in df_ret2:
                    gtin.writerow([i])


def delete_cont(): #apaga o gtin da tabela de contigencia se já existe resultado da cosmos.

    import connection

    with open('RES_Cont_' + ARQUIVO + '.csv', newline='') as f:
        gtins = csv.reader(f, delimiter=';')

        for l in gtins:
            g = (str(', '.join(l)))
            print(g)

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



        with open('RES_Cont_' + ARQUIVO + '.csv', 'r+') as f:
        #with open(ARQUIVO + '.csv', 'r+') as f:
            new_f = []
            new_f = f.readlines()
            f.seek(0)
            if new_f == []:
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(now, 'Scheduler_Cosmos - Arquivos encontrados na busca na API: lista vazia')
            for l in range(len(new_f)):
                print(g)
                if g not in new_f[l]:
                    print(new_f[l]+ ' gravado')
                    f.write(new_f[l])
                else:
                    print(new_f[l] + ' apagado')
            f.truncate()


def scheduler_cosmos():

    schedule.every(14400).seconds.do(ret_cosmos)
    schedule.every(5000).seconds.do(delete_cont)

    while True:

        schedule.run_pending()
        time.sleep(5)

