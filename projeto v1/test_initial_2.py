def conexao():
    import connection

    connection = connection.conexao()
    cursor = connection.cursor()
    cursor.execute("SELECT * from cnpj order by id_cnpj desc")
    id_result = cursor.fetchone()
    id_cnpj_in = id_result[0]
    id_cnpj = id_cnpj_in + 1
    return id_cnpj

def test_de_conexao():

    assert conexao != None

