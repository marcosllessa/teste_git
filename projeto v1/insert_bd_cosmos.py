import connection
import os
import json
from bd import BancoDeDados

connection = connection.conexao()

path = 'C:/Troca/gtin/python/ean/'
j = os.listdir(path)

for i in range(len(j)):
    arq = j[i]
    with open(path + arq, 'r', encoding='utf-8') as f:
        resposta = json.load(f)
        try:
            description = resposta['description']
        except:
            description = None

        try:
            gtin_in = resposta['gtin']
        except:
            gtin_in = None

        try:
            thumbnail = resposta['thumbnail']
        except:
            thumbnail = None

        try:
            width = resposta['width']
        except:
            width = None

        try:
            height = resposta['height']
        except:
            height = None

        try:
            length = resposta['length']
        except:
            length = None

        try:
            net_weight = resposta['net_weight']
        except:
            net_weight = None

        try:
            gross_weight = resposta['gross_weight']
        except:
            gross_weight = None

        try:
            created_at = resposta['created_at']
        except:
            created_at = None

        try:
            updated_at = resposta['updated_at']
        except:
            updated_at = None

        try:
            price = resposta['price']
        except:
            price = None

        try:
            avg_price = resposta['avg_price']
        except:
            avg_price = None

        try:
            max_price = resposta['max_price']
        except:
            max_price = None

        try:
            min_price = resposta['min_price']
        except:
            min_price = None


        '''Os dados que as variáveis abaixo recebem, vêm da classe BancoDeDados do arquivo bd.py'''

        s_gtins = BancoDeDados()
        sg = s_gtins.f_gtins(resposta)
        gtins = sg
        c_gtins_type_packaging = s_gtins.c_gtins_type_packaging
        c_gtins_quantity_packaging = s_gtins.c_gtins_quantity_packaging
        c_gtins_ballast = s_gtins.c_gtins_ballast
        c_gtins_layer = s_gtins.c_gtins_layer

        s_country = BancoDeDados()
        sc = s_country.f_country(resposta)
        country = sc
        countries_name = s_country.countries_name
        countries_icon_16 = s_country.countries_icon_16
        countries_icon_32 = s_country.countries_icon_32

        s_brand = BancoDeDados()
        sb = s_brand.f_brands(resposta)
        brand = sb
        brands_id = s_brand.brands_id
        brands_name = s_brand.brands_name
        brands_picture = s_brand.brands_picture
        brands_created_at = s_brand.brands_created_at
        brands_updated_at = s_brand.brands_updated_at
        brands_bsin = s_brand.brands_bsin
        brands_license = s_brand.brands_license
        brands_origin = s_brand.brands_origin
        brands_supplier_id = s_brand.brands_supplier_id
        brands_supplier_verified = s_brand.brands_supplier_verified
        brands_impressions_count = s_brand.brands_impressions_count
        brands_status = s_brand.brands_status
        brands_owner_id = s_brand.brands_owner_id



        try:
            origin = resposta['origin']
        except:
            origin = None

        try:
            barcode_image = resposta['barcode_image']
        except:
            barcode_image = None

        try:
            id = resposta['id']
        except:
            id = None

        try:
            url = resposta['url']
        except:
            url = None




        if gtin_in != None:
            gtin = str(gtin_in)
            cursor = connection.cursor()  # cria um cursor
            cursor.execute("SELECT * from gtin_data where gtin =" + gtin)  # consulta sql
            result = cursor.fetchone()  # busca o resultado da consulta



            '''Testa se o gtin já existe no banco. Se não existe, insere.'''

            if result == None:
                desc = description
                cursor.execute("SELECT * from gtin_data order by id_gtin desc")
                id_result = cursor.fetchone()
                id_gtin_in = id_result[0]
                id_gtin = id_gtin_in + 1
                cursor.execute(
                    "insert into gtin_data values (:id_gtin, :description, :gtin, :thumbnail, :width, :height, :length, :net_weight, :gross_weight, :created_at, :updated_at, :price, :avg_price, :max_price, :min_price, :gtins, :origin, :barcode_image, :id, :brand, :url, :country,:brands_id, :brands_name, :brands_picture, :brands_created_at, :brands_updated_at, :brands_bsin, :brands_license, :brands_origin, :brands_supplier_id, :brands_supplier_verified, :brands_impressions_count, :brands_status, :brands_owner_id, :c_gtins_type_packaging, :c_gtins_quantity_packaging, :c_gtins_ballast, :c_gtins_layer, :countries_name, :countries_icon_16, :countries_icon_32)",
                    [id_gtin, description, gtin, thumbnail, width, height, length, net_weight, gross_weight, created_at,
                     updated_at, price, avg_price, max_price, min_price, gtins, origin, barcode_image, id, brand, url,
                     country, brands_id, brands_name, brands_picture, brands_created_at, brands_updated_at, brands_bsin,
                     brands_license, brands_origin, brands_supplier_id, brands_supplier_verified, brands_impressions_count,
                     brands_status, brands_owner_id, c_gtins_type_packaging, c_gtins_quantity_packaging, c_gtins_ballast,
                     c_gtins_layer, countries_name, countries_icon_16, countries_icon_32])
                cursor.execute("commit")
                print('Arquivo ' + arq + ' inserido no Banco de dados.')
            else:
                print(str(result[2]) + 'GTIN já existe no banco!')

        else:
            print('O arquivo não possui numero GTIN!')

