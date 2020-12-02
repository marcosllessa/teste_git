import xml.etree.ElementTree as ET
from random import randint
import random
import connection


'''GERA CNPJ ALEATÓRIO PARA EMISSOR E DESTINATARIO'''

def cnpj(self, punctuation = False):
    n = [random.randrange(10) for i in range(8)] + [0, 0, 0, 1]
    v = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]
    # calcula dígito 1 e acrescenta ao total
    s = sum(x * y for x, y in zip(reversed(n), v))
    d1 = 11 - s % 11
    if d1 >= 10:
      d1 = 0
    n.append(d1)
    # idem para o dígito 2
    s = sum(x * y for x, y in zip(reversed(n), v))
    d2 = 11 - s % 11
    if d2 >= 10:
      d2 = 0
    n.append(d2)
    if punctuation:
      return "%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d" % tuple(n)
    else:
      return "%d%d%d%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)

cnpj_e = ("\n".join([cnpj(True) for i in range(1)]))
cnpj_d = ("\n".join([cnpj(True) for i in range(1)]))


'''BUSCA NO BANCO DE DADOS ALEATORIAMENTE EAN, DESCRICAO E PRECO'''

connection = connection.conexao()
r = str(randint(1,9999))
cursor = connection.cursor()
cursor.execute("SELECT gtin, description,price from gtin_data where id_gtin =" + r + " and price is not null")


try:
    for gtin, description,price in cursor:
        EAN = gtin
        Prod = description
        price = price

    print('EAN: ', EAN, ' Prod: ', Prod, ' price: ', price)

    path = 'C:/Troca/gtin/python/nfe/'
    tree = ET.parse(path + 'schema.xml')
    root = tree.getroot()


    '''GERA A NOTA FISCAL'''

    for ide in root.findall(".//ide"):
        for nNF in ide.findall("./nNF"):
            nNF.text = str(randint(1,9999))
            print('NF :', nNF.text)


    for emit in root.findall(".//emit"):
        for CNPJ in emit.findall("./CNPJ"):
            CNPJ.text = str(cnpj_e)
            print('CNPJ_EMIT :', CNPJ.text)


    for dest in root.findall(".//dest"):
        for CNPJ in dest.findall("./CNPJ"):
            CNPJ.text = str(cnpj_d)
            print('CNPJ_DEST :', CNPJ.text)


    for det in root.iter('det'):
        for prod in root.iter('prod'):
            for cprod in root.iter('cProd'):
                cprod.text = str(randint(1,9999))
                print('Codigo :', cprod.text)
            for ean in root.iter('cEAN'):
                ean.text = str(EAN)
                print('EAN :', ean.text)
            for xProd in root.iter('xProd'):
                xProd.text = str(Prod)
                print('Descrição :', xProd.text)
            for NCM in root.iter('NCM'):
                print('NCM :', NCM.text)
            for vUnCom in root.iter('vUnCom'):
                vUn = price
                vUn = vUn.replace(',','.')
                vUn = vUn.replace('R$', '')
                vUn = vUn.strip()
                vUnCom.text = str(vUn)
                print('valorUn :', vUnCom.text)
            for qCom in root.iter('qCom'):
                qCom.text = str(randint(1,29))
                qtd = int(qCom.text)
                print('Qtd :', qCom.text)
            for vProd in root.iter('vProd'):
                total = (float(vUnCom.text)*qtd)
                vProd.text = str(round(total,2))
                print('Total :',vProd.text)
            for eant in root.iter('cEANTrib'):
                eant.text = str(EAN)
                print('EANTrib :', eant.text)
            for qTrib in root.iter('qTrib'):
                qTrib.text = str(qtd)
                print('qTrib :',qTrib.text)

        tree.write(path + cnpj_e+'.xml')

except:
    print('Produto sem preço')





