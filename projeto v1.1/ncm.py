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

            ncm_in = resposta
            if ncm_in != None or ncm_in != []:
                ncm_in = ncm_in['ncm']
                #print(i,ncm_in)

        except:
            ncm_in = None
            #print(i,' O arquivo json não possui informação - NCM: ', ncm_in)

        try:
            if ncm_in != None or ncm_in != []:
                code = ncm_in['code']
                #print(i,code)
        except:
            code = None
            #print('Sem informação')


        try:
            if ncm_in != None or ncm_in != []:
                description = ncm_in['description']
                #print(i, description)
        except:
            description = None
            #print('Sem informação')

        try:
            if ncm_in != None or ncm_in != []:
                full_description = ncm_in['full_description']
                #print(i, full_description)
        except:
            full_description = None
            #print('Sem informação')


        if ncm_in != None:
            ncm = str(ncm_in)
            gtin = str(gtin)
            cursor = connection.cursor()  # cria um cursor
            cursor.execute("SELECT * from ncm where gtin =" + gtin)  # consulta sql
            result = cursor.fetchone()  # busca o resultado da consulta
            print('O BD respondeu que esse código ainda não foi cadastrado', gtin)



            # Testa se o gtin já existe no banco. Se não existe, insere.

            if result == None:
                desc = description
                cursor.execute("SELECT * from ncm order by id_ncm desc")
                id_result = cursor.fetchone()
                id_ncm_in = id_result[0]
                id_ncm = id_ncm_in + 1
                cursor.execute(
                    "insert into ncm values (:id_ncm, :code, :description, :full_description, :gtin)",
                    [id_ncm, code, description, full_description, gtin])
                cursor.execute("commit")
                print('Arquivo ' + arq + ' inserido no Banco de dados.')
            else:
                print(str(result[1]) + ' NCM já existe no banco!')

        else:
            print(i,'O arquivo não possui informação de NCM!')