import xml.etree.ElementTree as ET

path = 'C:/Troca/gtin/python/nfe/'
tree = ET.parse(path+'44257887000173.xml')
root = tree.getroot()

lista = []
for levels in root.iter():
    level = levels.tag
    level = level.replace('{http://www.portalfiscal.inf.br/nfe}','')
    l = (level, levels.text)
    lista.append(l)

dic = {}
for a, b in lista:
    dic.setdefault(a,[]).append(b)

nota = []
produtos = {}
for lista in range(len(dic['xProd'])):
    produtos.clear()
    produtos['cnpj'] = dic['CNPJ'][0]
    produtos['NF'] = dic['nNF'][0]
    produtos['EAN'] = dic['cEAN'][lista]
    produtos['Prod'] = dic['xProd'][lista]
    produtos['NCM'] = dic['NCM'][lista]
    produtos['CFOP'] = dic['CFOP'][lista]
    produtos['valorUn'] = dic['vUnCom'][lista]
    produtos['valorProd'] = dic['vProd'][lista]
    nota.append(produtos.copy())

    print(nota[lista])
