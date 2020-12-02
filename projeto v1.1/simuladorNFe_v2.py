import xml.etree.ElementTree as ET
from random import randint
import random
import connection


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



i = 0
itens = 10
path = 'C:/Troca/gtin/python/nfe/'
connection = connection.conexao()

root = ET.Element('NFe')
inf = ET.SubElement(root, 'infNFe')

ide = ET.SubElement(inf, 'ide')
nNF = ET.SubElement(ide, 'nNF')
nNF.text = str(randint(1, 9999))

emit = ET.SubElement(inf, 'emit')
CNPJ = ET.SubElement(emit, 'CNPJ')
CNPJ.text = str(cnpj_e)

dest = ET.SubElement(inf, 'dest')
CNPJ = ET.SubElement(dest, 'CNPJ')
CNPJ.text = str(cnpj_d)

while i <= (itens-1):
    x = i + 1
    r = str(randint(1, 9999))
    cursor = connection.cursor()
    cursor.execute("SELECT gtin, description,price from gtin_data where id_gtin =" + r)
    try:

        for gtin, description, price in cursor:
            EAN = gtin
            Prod = description
            price = price

        tag = root.findall(".//infNFe")
        det = ET.SubElement(inf,'det')
        det.set('nItem', str(x))

        prod = ET.SubElement(det, 'prod')
        cProd = ET.SubElement(prod, 'cProd')
        cProd.text = str(randint(1, 9999))

        cEAN = ET.SubElement(prod, 'cEAN')
        cEAN.text = str(EAN)
        i = i + 1
        xProd = ET.SubElement(prod, 'xProd')
        xProd.text = str(Prod)

        NCM = ET.SubElement(prod, 'NCM')

        vUnCom = ET.SubElement(prod, 'vUnCom')
        vUn = price
        vUn = vUn.replace(',', '.')
        vUn = vUn.replace('R$', '')
        vUn = vUn.strip()
        vUnCom.text = str(vUn)

        qCom = ET.SubElement(prod, 'qCom')
        qCom.text = str(randint(1, 29))
        qtd = int(qCom.text)

        vProd = ET.SubElement(prod, 'vProd')
        total = (float(vUnCom.text) * qtd)
        vProd.text = str(round(total, 2))

        cEANTrib = ET.SubElement(prod, 'cEANTrib')
        cEANTrib.text = str(EAN)

        qTrib = ET.SubElement(prod, 'qTrib')
        qTrib.text = str(qtd)
    except:
        i = i


r = ET.tostring(root).decode()
roo = ET.fromstring(r)
tree = ET.ElementTree(roo)
print(ET.tostring(root).decode())
tree.write(path + cnpj_e + ".xml", encoding="utf-8", xml_declaration=True)



