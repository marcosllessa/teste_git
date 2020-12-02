import connection
import csv
import json


connection = connection.conexao()

with open('empresa.csv', newline='', encoding="utf8") as csvfile:

    reader = csv.DictReader(csvfile)
    i = 0
    for row in reader:
        i = i+1
        #id_cnpj = i
        cnpj = row['cnpj']
        identificador_matriz_filial = row['identificador_matriz_filial']
        razao_social = row['razao_social']
        nome_fantasia = row['nome_fantasia']
        situacao_cadastral = row['situacao_cadastral']
        data_situacao_cadastral = row['data_situacao_cadastral']
        motivo_situacao_cadastral = row['motivo_situacao_cadastral']
        nome_cidade_exterior = row['nome_cidade_exterior']
        codigo_natureza_juridica = row['codigo_natureza_juridica']
        data_inicio_atividade = row['data_inicio_atividade']
        cnae_fiscal = row['cnae_fiscal']
        descricao_tipo_logradouro = row['descricao_tipo_logradouro']
        logradouro = row['logradouro']
        numero = row['numero']
        complemento = row['complemento']
        bairro = row['bairro']
        cep = row['cep']
        uf = row['uf']
        codigo_municipio = row['codigo_municipio']
        municipio = row['municipio']
        ddd_telefone_1 = row['ddd_telefone_1']
        ddd_telefone_2 = row['ddd_telefone_2']
        ddd_fax = row['ddd_fax']
        qualificacao_do_responsavel = row['qualificacao_do_responsavel']
        capital_social = row['capital_social']
        porte = row['porte']
        opcao_pelo_simples = row['opcao_pelo_simples']
        data_opcao_pelo_simples = row['data_opcao_pelo_simples']
        data_exclusao_do_simples = row['data_exclusao_do_simples']
        situacao_especial = row['situacao_especial']
        data_situacao_especial = row['data_situacao_especial']
        opcao_pelo_mei = row['opcao_pelo_mei']
        print(i)

        cursor = connection.cursor()
        cursor.execute("SELECT * from cnpj order by id_cnpj desc")
        id_result = cursor.fetchone()
        id_cnpj_in = id_result[0]
        id_cnpj = id_cnpj_in + 1

        sql = 'insert into cnpj (id_cnpj,cnpj,identificador_matriz_filial,razao_social,nome_fantasia,situacao_cadastral,data_situacao_cadastral,motivo_situacao_cadastral,nome_cidade_exterior,codigo_natureza_juridica,data_inicio_atividade,cnae_fiscal,descricao_tipo_logradouro,logradouro,numero,complemento,bairro,cep,uf,codigo_municipio,municipio,ddd_telefone_1,ddd_telefone_2,ddd_fax,qualificacao_do_responsavel,capital_social,porte,opcao_pelo_simples,data_opcao_pelo_simples,data_exclusao_do_simples,situacao_especial,data_situacao_especial,opcao_pelo_mei) values (:id_cnpj,:cnpj,:identificador_matriz_filial,:razao_social,:nome_fantasia,:situacao_cadastral,:data_situacao_cadastral,:motivo_situacao_cadastral,:nome_cidade_exterior,:codigo_natureza_juridica,:data_inicio_atividade,:cnae_fiscal,:descricao_tipo_logradouro,:logradouro,:numero,:complemento,:bairro,:cep,:uf,:codigo_municipio,:municipio,:ddd_telefone_1,:ddd_telefone_2,:ddd_fax,:qualificacao_do_responsavel,:capital_social,:porte,:opcao_pelo_simples,:data_opcao_pelo_simples,:data_exclusao_do_simples,:situacao_especial,:data_situacao_especial,:opcao_pelo_mei)'
        val = [id_cnpj,cnpj,identificador_matriz_filial,razao_social,nome_fantasia,situacao_cadastral,data_situacao_cadastral,motivo_situacao_cadastral,nome_cidade_exterior,codigo_natureza_juridica,data_inicio_atividade,cnae_fiscal,descricao_tipo_logradouro,logradouro,numero,complemento,bairro,cep,uf,codigo_municipio,municipio,ddd_telefone_1,ddd_telefone_2,ddd_fax,qualificacao_do_responsavel,capital_social,porte,opcao_pelo_simples,data_opcao_pelo_simples,data_exclusao_do_simples,situacao_especial,data_situacao_especial,opcao_pelo_mei]
        cursor.execute(sql, val)
        cursor.execute("commit")
print('fim')


