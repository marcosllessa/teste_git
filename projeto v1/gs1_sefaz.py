import connection
import csv



connection = connection.conexao()




with open('parte4.csv', newline='', encoding="utf8") as csvfile:

    reader = csv.DictReader(csvfile, delimiter=';', fieldnames=None, restkey=None, restval=None)
    i = 0
    for row in reader:
        i = i+1
        try:
            SEQ_GTIN = int(row['SEQ_GTIN'])
            #print(type(SEQ_GTIN))
            NUM_CODIGO = int(row['NUM_CODIGO'])
            #print(type(NUM_CODIGO))
            NUM_TIPO_GTIN = int(row['NUM_TIPO_GTIN'])
            #print(type(NUM_TIPO_GTIN))
            NOM_PRODUTO = row['NOM_PRODUTO']
            #print(type(NOM_PRODUTO))
            TIP_PRODUTO = row['TIP_PRODUTO']
            #print(type(TIP_PRODUTO))
            NUM_PREFIXO_GS1 = int(row['NUM_PREFIXO_GS1'])
            #print(type(NUM_PREFIXO_GS1))
            NUM_PREFIXO_EMPRESA = int(row['NUM_PREFIXO_EMPRESA'])
            #print(type(NUM_PREFIXO_EMPRESA))
            COD_NCM = row['COD_NCM']
            if COD_NCM == '' or COD_NCM == None:
                COD_NCM = None
            else:
                COD_NCM = float(row['COD_NCM'])
                COD_NCM = int(COD_NCM)
            #print(type(COD_NCM), COD_NCM)
            SIT_SITUACAO = int(row['SIT_SITUACAO'])
            #print(type(SIT_SITUACAO))
            DAT_CRIACAO = row['DAT_CRIACAO']
            #print(type(DAT_CRIACAO))
            NUM_CNPJ = float(row['NUM_CNPJ'])
            #print(type(NUM_CNPJ))
            DAT_SITUACAO = row['DAT_SITUACAO']
            #print(type(DAT_SITUACAO))
            NUM_SEQ_UNICO = int(row['NUM_SEQ_UNICO'])
            #print(type(NUM_SEQ_UNICO))
            DSC_IMG_URL = row['DSC_IMG_URL']
            #print(type(DSC_IMG_URL))
            NUM_CPF = row['NUM_CPF']
            if NUM_CPF == None or NUM_CPF == '':
                NUM_CPF = None
            else:
                NUM_CPF = int(row['NUM_CPF'])
            #print(type(NUM_CPF),NUM_CPF,'cpf')
        except:
            print('Erro de tipo de dados')

        NUM_CODIGO = str(NUM_CODIGO)
        #print(type(NUM_CODIGO))
        cursor = connection.cursor()  # cria um cursor
        cursor.execute("SELECT NUM_CODIGO from gtin_sefaz where NUM_CODIGO =" + NUM_CODIGO)  # consulta sql
        result = cursor.fetchone()  # busca o resultado da consulta
        NUM_CODIGO = int(NUM_CODIGO)


        try:
            if result == None:

                cursor = connection.cursor()
                cursor.execute("SELECT seq_id from gtin_sefaz order by seq_id desc")
                id_result = cursor.fetchone()
                seq_id_in = id_result[0]
                SEQ_ID = seq_id_in + 1

                sql = 'insert into gtin_sefaz (SEQ_ID,SEQ_GTIN,NUM_CODIGO,NUM_TIPO_GTIN,NOM_PRODUTO,TIP_PRODUTO,NUM_PREFIXO_GS1,NUM_PREFIXO_EMPRESA,COD_NCM,SIT_SITUACAO,DAT_CRIACAO,DAT_SITUACAO,NUM_SEQ_UNICO,DSC_IMG_URL,NUM_CPF,NUM_CNPJ) values (:SEQ_ID,:SEQ_GTIN,:NUM_CODIGO,:NUM_TIPO_GTIN,:NOM_PRODUTO,:TIP_PRODUTO,:NUM_PREFIXO_GS1,:NUM_PREFIXO_EMPRESA,:COD_NCM,:SIT_SITUACAO,:DAT_CRIACAO,:DAT_SITUACAO,:NUM_SEQ_UNICO,:DSC_IMG_URL,:NUM_CPF,:NUM_CNPJ)'
                val = [SEQ_ID,SEQ_GTIN,NUM_CODIGO,NUM_TIPO_GTIN,NOM_PRODUTO,TIP_PRODUTO,NUM_PREFIXO_GS1,NUM_PREFIXO_EMPRESA,COD_NCM,SIT_SITUACAO,DAT_CRIACAO,DAT_SITUACAO,NUM_SEQ_UNICO,DSC_IMG_URL,NUM_CPF,NUM_CNPJ]
                cursor.execute(sql, val)
                cursor.execute("commit")

                print(i)

            else:
                print(str(result[0]) + ' - GTIN já existe no banco!')
        except:
            print('Algum erro...')

    else:
        print('O arquivo não possui numero GTIN!')
print('fim', i)