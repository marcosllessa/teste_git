import connection
import pandas as pd

ARQUIVO = 'busca_gtins'
path = 'C:/Troca/gtin/python/eanGS1/'
path_error = 'C:/Troca/gtin/python/error_eanGS1/'
df_ean = pd.read_csv(ARQUIVO + '.csv', sep=',')
df_ret2 = []

connection = connection.conexao()

for i in range(len(df_ean)):
    gtin = str(int(df_ean.iloc[i])).zfill(14)

    #gtin = input('Digite o GTIN : ')

    cursor = connection.cursor()  # cria um cursor
    cursor.execute("SELECT * from gs1_dados where gtin =" + gtin)  # consulta sql
    result = cursor.fetchone()  # busca o resultado da consulta

    if result == None:
        print(i," Nenhum Resultado...Será inserido no BD")
        cont_gtin = gtin
        cursor.execute("SELECT * from cont_gtin where gtin ="+ cont_gtin)
        res = cursor.fetchone()
        if res != None:
            print("GTIN foi inserido na base de dados para busca posterior.")
        else:
            cursor.execute("SELECT * from cont_gtin order by id_gtin desc")
            id_result = cursor.fetchone()
            id_gtin_in = id_result[0]
            id_gtin = id_gtin_in + 1
            cursor.execute("insert into cont_gtin values (:id_gtin, :cont_gtin)", [id_gtin, gtin])
            cursor.execute("commit")

    else:
        print(result)

connection.close()
