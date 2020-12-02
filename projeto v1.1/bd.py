class BancoDeDados:
    '''
    Essa classe  insere no Banco de Dados as informações referentes a gtin, country e brands retornados da busca de GTIN's na
    API Cosmos. Trabalha em conjunto com o arquivo insert_bd_cosmos.py
    '''


    def f_gtins(self, resposta):

        gtins = resposta

        try:
            gtins = gtins['gtins']
            # print(gtins)

            d_gtins = gtins[0]
            # print(d_gtins)
            valores = []
            gtins = 'inserido nos respectivos campos'

            for k, v in d_gtins.items():
                c = (k, v)
                valores.append(c)

            gtins_it = valores[1]
            gtin_list = gtins_it[1]
            global c_gtins
            c_gtins = []
            dictc_gtins = {}
            for k, v in gtin_list.items():
                c = (k, v)
                c_gtins.append(c)
                # print(c_gtins)
                dictc_gtins = dict(c_gtins)

            w = []
            for k, v in dictc_gtins.items():
                desc = (k, v)
                w.append(desc)
            dictgtins = dict(w)
            # print(dictgtins['type_packaging'])

            self.gtin = 'inserido nos respectivos campos'
            self.c_gtins_type_packaging = None
            self.c_gtins_quantity_packaging = None
            self.c_gtins_ballast = None
            self.c_gtins_layer = None

            try:
                if dictgtins['type_packaging'] != None:
                    self.c_gtins_type_packaging = dictgtins['type_packaging']
            except:
                self.c_gtins_type_packaging = None

            try:
                if dictgtins['quantity_packaging'] != None:
                    self.c_gtins_quantity_packaging = dictgtins['quantity_packaging']
            except:
                self.c_gtins_quantity_packaging = None

            try:
                if dictgtins['ballast'] != None:
                    self.c_gtins_ballast = dictgtins['ballast']
            except:
                self.c_gtins_ballast = None

            try:
                if dictgtins['layer'] != None:
                    self.c_gtins_layer = dictgtins['layer']
            except:
                self.c_gtins_layer = None

            # print(gtin, c_gtins_type_packaging, c_gtins_quantity_packaging, c_gtins_ballast, c_gtins_layer)

        except:

            gtins = []

            if gtins == None or gtins == []:
                self.gtins = 'sem dados'
                self.c_gtins_type_packaging = None
                self.c_gtins_quantity_packaging = None
                self.c_gtins_ballast = None
                self.c_gtins_layer = None


    def f_country(self, resposta):

        country = resposta

        try:
            country = country['country']
            w = []
            for k, v in country.items():
                desc = (k, v)
                w.append(desc)
                dictcountry = dict(w)


            self.country = 'inserido nos respectivos campos'

            try:
                if dictcountry['countries_name'] != None:
                    self.countries_name = dictcountry['countries_name']
            except:
                self.countries_name = None

            try:
                if dictcountry['countries_icon_16'] != None:
                    self.countries_icon_16 = dictcountry['countries_icon_16']
            except:
                self.countries_icon_16 = None

            try:
                if dictcountry['countries_icon_32'] != None:
                    self.countries_icon_32 = dictcountry['countries_icon_32']
            except:
                self.countries_icon_32 = None

            '''print(country, countries_name,
                  countries_icon_16, countries_icon_32)'''


        except:
            country = []

            if country == None or country == []:
                self.country = 'sem dados'
                self.countries_name = None
                self.countries_icon_16 = None
                self.countries_icon_32 = None

                '''print(country,countries_name,
                  countries_icon_16,countries_icon_32)'''

    def f_brands(self, resposta):

        brand = resposta

        try:
            brand = brand['brand']
            w = []
            for k, v in brand.items():
                desc = (k, v)
                w.append(desc)
                dictbrands = dict(w)

            self.brands = 'inserido nos respectivos campos'

            try:
                if dictbrands['id'] != None:
                    self.brands_id = brand['id']
            except:
                self.brands_id = None

            try:
                if dictbrands['name'] != None:
                    self.brands_name = dictbrands['name']
            except:
                self.brands_name = None

            try:
                if dictbrands['picture'] != None:
                    self.brands_picture = dictbrands['picture']
            except:
                self.brands_picture = None

            try:
                if dictbrands['created_at'] != None:
                    self.brands_created_at = dictbrands['created_at']
            except:
                self.brands_created_at = None

            try:
                if dictbrands['updated_at'] != None:
                    self.brands_updated_at = dictbrands['updated_at']
            except:
                self.brands_updated_at = None

            try:
                if dictbrands['bsin'] != None:
                    self.brands_bsin = dictbrands['bsin']
            except:
                self.brands_bsin = None

            try:
                if dictbrands['license'] != None:
                    self.brands_license = dictbrands['license']
            except:
                self.brands_license = None

            try:
                if dictbrands['origin'] != None:
                    self.brands_origin = dictbrands['origin']
            except:
                self.brands_origin = None

            try:
                if dictbrands['supplier_id'] != None:
                    self.brands_supplier_id = dictbrands['supplier_id']
            except:
                self.brands_supplier_id = None

            try:
                if dictbrands['supplier_verified'] != None:
                    self.brands_supplier_verified = dictbrands['supplier_verified']
            except:
                self.brands_supplier_verified = None

            try:
                if dictbrands['impressions_count'] != None:
                    self.brands_impressions_count = dictbrands['impressions_count']
            except:
                self.brands_impressions_count = None

            try:
                if dictbrands['status'] != None:
                    self.brands_status = dictbrands['status']
            except:
                self.brands_status = None

            try:
                if dictbrands['owner_id'] != None:
                    self.brands_owner_id = dictbrands['owner_id']
            except:
                self.brands_owner_id = None

            '''print(brands, brands_id, brands_name, brands_picture,
                  brands_created_at, brands_updated_at, brands_bsin,
                  brands_license, brands_origin, brands_supplier_id,
                  brands_supplier_verified, brands_impressions_count,
                  brands_status, brands_owner_id)'''

        except:
            brand = []
            if brand == None or brand == []:
                self.brand = 'sem dados'
                self.brands_id = None
                self.brands_name = None
                self.brands_picture = None
                self.brands_created_at = None
                self.brands_updated_at = None
                self.brands_bsin = None
                self.brands_license = None
                self.brands_origin = None
                self.brands_supplier_id = None
                self.brands_supplier_verified = None
                self.brands_impressions_count = None
                self.brands_status = None
                self.brands_owner_id = None

                '''print(brand, brands_id, brands_name, brands_picture,
                  brands_created_at, brands_updated_at, brands_bsin,
                  brands_license, brands_origin, brands_supplier_id,
                  brands_supplier_verified, brands_impressions_count,
                  brands_status, brands_owner_id)'''