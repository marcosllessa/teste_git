import xml.etree.ElementTree as ET
import connection


connection = connection.conexao()


PATH = 'GS1BRcopia.xml'

tree = ET.parse(PATH)
root = tree.getroot()
id_segmento = 0
id_familia = 0
id_classe = 0
id_bloco = 0

for child in root.findall("segment"):
    cursor = connection.cursor()
    cursor.execute("SELECT * from gpc_segmento order by id_segmento desc")
    id_result = cursor.fetchone()
    id_segmento_in = id_result[0]
    id_segmento = id_segmento_in + 1
    gpc_segmento_id_segmento = id_segmento
    '''Mostra todos os segmentos'''
    if 'code' in child.keys():
        segmento = []
        s = child.items()
        segmento.append(s)
        cod_segmento = segmento[0][0][1]
        desc_segmento = segmento[0][1][1]
        print('segmento: ',cod_segmento,desc_segmento)

        '''INSERE SEGMENTO - tabela gpc_segmento'''
        cursor = connection.cursor()
        sql = 'insert into gpc_segmento (id_segmento,cod_segmento,desc_segmento) values (:id_segmento,:cod_segmento,:desc_segmento)'
        val = [id_segmento, cod_segmento, desc_segmento]
        cursor.execute(sql, val)  # consulta sql
        cursor.execute("commit")
        print('Inserido novo segmento')


    for family in child.findall("family"):
        cursor = connection.cursor()
        cursor.execute("SELECT * from gpc_familia order by id_familia desc")
        id_result = cursor.fetchone()
        id_familia_in = id_result[0]
        id_familia = id_familia_in + 1
        gpc_familia_id_familia = id_familia
        '''Mostra todas as famílias'''
        if 'code' in family.keys():
            familia = []
            f = family.items()
            familia.append(f)
            cod_familia = familia[0][0][1]
            desc_familia = familia[0][1][1]
            print('familia: ', cod_familia, desc_familia)

            '''INSERE FAMILIA - tabela gpc_familia'''
            cursor = connection.cursor()
            sql = 'insert into gpc_familia (desc_familia,cod_familia,id_familia,gpc_segmento_id_segmento,cod_segmento,desc_segmento) values (:desc_familia,:cod_familia,:id_familia,:gpc_segmento_id_segmento,:cod_segmento,:desc_segmento)'
            val = [desc_familia, cod_familia, id_familia, gpc_segmento_id_segmento, cod_segmento, desc_segmento]
            cursor.execute(sql, val)  # consulta sql
            cursor.execute("commit")
            print('Inserido nova familia')


        for clas in family.findall("class"):
            cursor = connection.cursor()
            cursor.execute("SELECT * from gpc_classe order by id_classe desc")
            id_result = cursor.fetchone()
            id_classe_in = id_result[0]
            id_classe = id_classe_in + 1
            gpc_classe_id_classe = id_classe
            '''Mostra todas as classes'''
            if 'code' in clas.keys():
                classe = []
                c = clas.items()
                classe.append(c)
                cod_classe = classe[0][0][1]
                desc_classe = classe[0][1][1]
                print('classe: ', cod_classe, desc_classe)

                '''INSERE CLASSE - tabela gpc_classe'''
                cursor = connection.cursor()
                sql = 'insert into gpc_classe (desc_classe,cod_classe,id_classe,desc_familia,cod_familia,gpc_familia_id_familia,gpc_segmento_id_segmento,cod_segmento,desc_segmento) values (:desc_classe,:cod_classe,:id_classe,:desc_familia,:cod_familia,:gpc_familia_id_familia,:gpc_segmento_id_segmento,:cod_segmento,:desc_segmento)'
                val = [desc_classe,cod_classe,id_classe,desc_familia,cod_familia, gpc_familia_id_familia,gpc_segmento_id_segmento,cod_segmento,desc_segmento]
                cursor.execute(sql, val)  # consulta sql
                cursor.execute("commit")
                print('Inserido nova classe')

            for brick in clas.findall("brick"):
                cursor = connection.cursor()
                cursor.execute("SELECT * from gpc_bloco order by id_bloco desc")
                id_result = cursor.fetchone()
                id_bloco_in = id_result[0]
                id_bloco = id_bloco_in + 1
                '''Mostra todos os blocos'''
                if 'code' in brick.keys():
                    bloco = []
                    b = brick.items()
                    bloco.append(b)

                    cod_bloco = bloco[0][0][1]
                    desc_bloco = bloco[0][1][1]
                    def_bloco = bloco[0][2][1]
                    print(id_bloco, cod_bloco,desc_bloco)

                    '''INSERE BLOCO - tabela gpc_bloco'''
                    cursor = connection.cursor()
                    sql = 'insert into gpc_bloco (def_bloco,desc_bloco,cod_bloco,id_bloco,desc_classe,cod_classe,gpc_classe_id_classe,desc_familia,cod_familia,gpc_familia_id_familia,gpc_segmento_id_segmento,cod_segmento,desc_segmento) values (:def_bloco,:desc_bloco,:cod_bloco,:id_bloco,:desc_classe,:cod_classe,:gpc_classe_id_classe,:desc_familia,:cod_familia,:gpc_familia_id_familia,:gpc_segmento_id_segmento,:cod_segmento,:desc_segmento)'
                    val = [def_bloco,desc_bloco,cod_bloco,id_bloco,desc_classe,cod_classe,gpc_classe_id_classe,desc_familia,cod_familia,gpc_familia_id_familia,gpc_segmento_id_segmento, cod_segmento,desc_segmento]
                    cursor.execute(sql,val)  # consulta sql
                    cursor.execute("commit")
                    print('Inserido novo bloco')



print('Fim  - Total de Registros: ', id_bloco)
