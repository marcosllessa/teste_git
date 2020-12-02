import connection
import os
import json

connection = connection.conexao()

path = 'C:/Troca/gtin/python/eanGS1/'
j = os.listdir(path)
for i in range(len(j)):
    arq = j[i]
    with open(path + arq, 'r', encoding='utf-8') as f:
        resposta = json.load(f)

        try:

            gtin = resposta
            if gtin != None or gtin != []:
                gtin = gtin['gtin']
                print(i,gtin)
        except:
            gtin = None
            print(i,' O arquivo json não possui informação - GTIN: ', gtin)

        try:

            gpc_in = resposta
            if gpc_in != None or gpc_in != []:
                gpc_in = gpc_in['gpc']
                #print(i,gpc_in)
                #print('______')

        except:
            gpc_in = None
            #print(i,' O arquivo json não possui informação - GPC: ', gpc_in)
            #print('______')

        try:

            if gpc_in != None or gpc_in != []:
                code = gpc_in['code']
                #print(i,code)
                #print('______')

        except:
            code = None
            #print('Code: ',code)
            #print('______')

        try:

            if gpc_in != None or gpc_in != []:
                description = gpc_in['description']
                #print(i,description)
                #print('______')

        except:
            description = None
            #print('description :',description)
            #print('______')

        if gpc_in != None:
            ncm = str(gpc_in)
            gtin = str(gtin)
            cursor = connection.cursor()  # cria um cursor
            cursor.execute("SELECT * from gpc where gtin =" + gtin)  # consulta sql
            result = cursor.fetchone()  # busca o resultado da consulta
            print('O BD respondeu que esse código ainda não foi cadastrado ', result)



            # Testa se o gtin já existe no banco. Se não existe, insere.

            if result == None:
                desc = description
                cursor.execute("SELECT * from gpc order by id_gpc desc")
                id_result = cursor.fetchone()
                id_gpc_in = id_result[0]
                id_gpc = id_gpc_in + 1
                cursor.execute(
                    "insert into gpc values (:id_gpc, :code, :description, :gtin)",
                    [id_gpc, code, description, gtin])
                cursor.execute("commit")
                print('Arquivo ' + arq + ' inserido no Banco de dados.')
            else:
                print(str(result[1]) + ' GPC já existe no banco!')

        else:
            print(i,'O arquivo não possui informação de GPC!')