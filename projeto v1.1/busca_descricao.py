import connection

connection = connection.conexao()

desc = input('Digite a descrição do produto : ').upper()  # transforma o que foi digitado em maiúscula

cursor = connection.cursor()  # cria um cursor
cursor.execute("SELECT * from data_gtin where UPPER (description) like :d", d='%' + desc + '%')  # faz a consulta sql
result = cursor.fetchall()  # busca o resultado da consulta

if result == []:
    print("Nenhum Resultado")
    exit
else:
    for i in range(len(result)):
        print(result[i])

connection.close()
