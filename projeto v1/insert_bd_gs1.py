import connection
import os
import json


connection = connection.conexao()

path = 'C:/Troca/gtin/python/eanGS1/'
j = os.listdir(path)

additTradeItemDescription = None
measurementUnitCode_1 = None
netvalue = None
originalValue = None
valor = None
measurementUnitCode = None



for i in range(len(j)):
    arq = j[i]
    print(arq)
    with open(path + arq, 'r', encoding='utf-8') as f:
        try:
            resposta = json.load(f)
            #print(resposta)
            gs1 = resposta
        except:
            print('algum erro')
        try:
            if 'product' in gs1:
                gs1Prod = gs1['product']
            if gs1Prod != None:

                try:
                    gs1TradeItemIdentificationKey = gs1Prod['gs1TradeItemIdentificationKey']
                    if gs1TradeItemIdentificationKey != None:

                        gtin = gs1TradeItemIdentificationKey['gtin']
                        fixedLengthGtin = int(gs1TradeItemIdentificationKey['fixedLengthGtin'])
                        gs1TradeItemIdentificationKey = gs1TradeItemIdentificationKey['gs1TradeItemIdentificationKeyCode']
                except:

                    gs1TradeItemIdentificationKeyCode = None
                    gtin = None
                    fixedLengthGtin = None

                try:
                    if 'tradeItemDescriptionInformation' in gs1Prod:
                        tradeItemDescriptionInformation = gs1Prod['tradeItemDescriptionInformation']
                        if 'tradeItemDescription' in tradeItemDescriptionInformation:
                            tradeItemDescription = tradeItemDescriptionInformation['tradeItemDescription']
                        if tradeItemDescription == ' ' or tradeItemDescription == None \
                                or tradeItemDescription == []:
                            tradeItemDescription = None

                        if 'additionalTradeItemDescription' in tradeItemDescriptionInformation:
                            additTradeItemDescription = tradeItemDescriptionInformation['additionalTradeItemDescription']

                        if additTradeItemDescription == ' ' or additTradeItemDescription == None \
                                or additTradeItemDescription == []:
                            additTradeItemDescription = None

                except:
                    if 'tradeItemDescription' in tradeItemDescriptionInformation:
                        tradeItemDescription = tradeItemDescriptionInformation['tradeItemDescription']
                    if 'additionalTradeItemDescription' in tradeItemDescriptionInformation:
                        additTradeItemDescription = tradeItemDescriptionInformation['additionalTradeItemDescription']




                try:
                    if 'childTradeItems' in gs1Prod:
                        childTradeItems = gs1Prod['childTradeItems']
                        if childTradeItems == [] or childTradeItems == None:


                            childTradeItems = None

                except:

                    childTradeItems = gs1Prod['childTradeItems']


                try:
                    if 'referencedFileInformations' in gs1Prod:
                        referencedFileInformations = gs1Prod['referencedFileInformations']
                        referencedFileInformations = referencedFileInformations[0]
                        if referencedFileInformations != [] or referencedFileInformations != None or referencedFileInformations != ' ':
                            if 'uniformResourceIdentifier' in referencedFileInformations:
                                uniformResourceIdentifier = referencedFileInformations['uniformResourceIdentifier']
                                if uniformResourceIdentifier != None or uniformResourceIdentifier !=[]:
                                    uniformResourceIdentifier = referencedFileInformations['uniformResourceIdentifier']
                            else:
                                uniformResourceIdentifier = None
                            if 'contentDescription' in referencedFileInformations:
                                contentDescription = referencedFileInformations['contentDescription']
                                if contentDescription == None or contentDescription == '' or contentDescription == []:

                                    contentDescription = None

                            else:
                                contentDescription = referencedFileInformations['contentDescription']
                            if 'fileName' in referencedFileInformations:
                                fileName = referencedFileInformations['fileName']
                                if fileName != None or fileName != '':
                                    fileName = referencedFileInformations['fileName']
                            else:
                                fileName = None
                            if 'referencedFileTypeCode' in referencedFileInformations:
                                referencedFileTypeCode = referencedFileInformations['referencedFileTypeCode']
                                if referencedFileTypeCode != None or referencedFileTypeCode != []:
                                    referencedFileTypeCode = referencedFileInformations['referencedFileTypeCode']
                            else:
                                referencedFileTypeCode = None
                            if 'featuredFile' in referencedFileInformations:
                                featuredFile = referencedFileInformations['featuredFile']
                                if featuredFile != None or featuredFile !=[]:
                                    featuredFile = referencedFileInformations['featuredFile']
                            else:
                                featuredFile = None

                except:

                    referencedFileInformations = None
                    uniformResourceIdentifier = None
                    contentDescription = None
                    fileName = None
                    referencedFileTypeCode = None
                    featuredFile = None

                try:
                    if 'gtinStatusCode' in gs1Prod:
                        gtinStatusCode = gs1Prod['gtinStatusCode']

                except:
                    gtinStatusCode = None

                try:
                    if 'brandNameInformation' in gs1Prod:
                        brandNameInformation = gs1Prod['brandNameInformation']
                        if 'brandName' in brandNameInformation:
                            brandName = brandNameInformation['brandName']
                    else:
                        brandName = None

                except:
                    brandNameInformation = None

                try:
                    if 'languageCode' in gs1Prod:
                        languageCode = gs1Prod['languageCode']

                except:
                    languageCode = None

                try:
                    if 'tradeItemWeight' in gs1Prod:
                        tradeItemWeight = gs1Prod['tradeItemWeight']

                        if 'grossWeight' in tradeItemWeight:
                            grossWeight = tradeItemWeight['grossWeight']
                            if 'measurementUnitCode' in grossWeight:
                                measurementUnitCode = grossWeight['measurementUnitCode']
                                if measurementUnitCode != [] or measurementUnitCode!= None:
                                    measurementUnitCode = grossWeight['measurementUnitCode']

                            else:
                                measurementUnitCode = None

                            if 'value' in grossWeight:
                                valor = grossWeight['value']
                                if valor != [] or valor != None:
                                    valor = grossWeight['value']
                            else:
                                valor = None

                            if 'originalValue' in grossWeight:
                                originalValue = grossWeight['originalValue']
                                if originalValue != [] or originalValue != None:
                                    originalValue = grossWeight['originalValue']
                            else:
                                originalValue = None

                        if 'netWeight' in tradeItemWeight:
                            netWeight = tradeItemWeight['netWeight']
                            if 'value' in netWeight:
                                netvalue = netWeight['value']
                                if netvalue != [] or netvalue != None:
                                    netvalue = netWeight['value']
                            else:
                                netvalue = None

                            if 'measurementUnitCode' in netWeight:
                                measurementUnitCode = netWeight['measurementUnitCode']
                                if measurementUnitCode != [] or measurementUnitCode != None:
                                    measurementUnitCode_1 = netWeight['measurementUnitCode']
                            else:
                                measurementUnitCode_1 = None

                except:
                    tradeItemWeight = None

                try:
                    if 'tradeItemMeasurements' in gs1Prod:
                        tradeItemMeasurements = gs1Prod['tradeItemMeasurements']
                        if 'depth' in tradeItemMeasurements:
                            depthAll = tradeItemMeasurements['depth']
                            if 'value' in depth:
                                depth_value = depth['value']
                                if depth_value == [] or depth_value == None:
                                    depth_value = None
                                else:
                                    depth_value = depth['value']
                            else:
                                depth_value = None

                            if 'measurementUnitCode' in depth:
                                depth_measurementUnitCode = depth['measurementUnitCode']
                                if depth_measurementUnitCode == [] or depth_measurementUnitCode == None:

                                    depth_measurementUnitCode = None
                                else:
                                    depth_measurementUnitCode = depth['measurementUnitCode']
                        else:
                            depthAll = None


                        if 'height' in tradeItemMeasurements:
                            height = tradeItemMeasurements['height']
                            if 'value' in height:
                                height_value = height['value']
                                if height_value == [] or height_value == None:
                                    height_value = None
                                else:
                                    height_value = height['value']

                            if 'measurementUnitCode' in height:
                                height_measurementUnitCode = height['measurementUnitCode']
                                if height_measurementUnitCode == [] or height_measurementUnitCode == None:
                                    height_measurementUnitCode = None
                                else:
                                    height_measurementUnitCode = height['measurementUnitCode']

                            else:
                                height_measurementUnitCode = None
                        else:
                            height = None

                        if 'netContent' in tradeItemMeasurements:
                            netContent = tradeItemMeasurements['netContent']
                            if 'value' in netContent:
                                netContent_value = netContent['value']
                                if netContent_value == [] or netContent_value == None:
                                    netContent_value = None
                                else:
                                    netContent_value = netContent['value']

                            else:
                                netContent_value = None

                            if 'measurementUnitCode' in netContent:
                                netContent_measurementUnitCode = netContent['measurementUnitCode']
                                if netContent_measurementUnitCode == [] or netContent_measurementUnitCode == None:
                                    netContent_measurementUnitCode = None
                                else:
                                    netContent_measurementUnitCode = netContent_measurementUnitCode['measurementUnitCode']
                            else:
                                netContent_measurementUnitCode = None
                        else:
                            netContent = None

                        if 'width' in tradeItemMeasurements:
                            width = tradeItemMeasurements['width']
                            if 'value' in width:
                                width_value = width['value']
                                if width_value == [] or width_value == None:
                                    width_value = None
                                else:
                                    width_value = width['value']

                            else:
                                width_value = None

                            if 'measurementUnitCode' in width:
                                width_measurementUnitCode = width['measurementUnitCode']
                                if width_measurementUnitCode == [] or width_measurementUnitCode == None:
                                    width_measurementUnitCode = None
                                else:
                                    width_measurementUnitCode = width['measurementUnitCode']
                            else:
                                width_measurementUnitCode = None
                        else:
                            width = None

                except:
                    tradeItemMeasurements = None
                    depth = None
                    depth_value = None
                    depth_measurementUnitCode = None
                    height = None
                    height_value = None
                    height_measurementUnitCode = None
                    netContent = None
                    netContent_value = None
                    netContent_measurementUnitCode = None
                    width = None
                    width_value = None
                    width_measurementUnitCode = None

                try:
                    if 'tradeItemClassification' in gs1Prod:
                        tradeItemClassification = gs1Prod['tradeItemClassification']
                        if 'gpcCategoryCode' in tradeItemClassification:
                            gpcCategoryCode = tradeItemClassification['gpcCategoryCode']
                            if gpcCategoryCode == [] or gpcCategoryCode == None:
                                gpcCode = None
                            else:
                                gpcCode = tradeItemClassification['gpcCategoryCode']
                        else:
                            gpcCode = None

                        if 'gpcCategoryName' in tradeItemClassification:
                            gpcCategoryName = tradeItemClassification['gpcCategoryName']
                            if gpcCategoryName == [] or gpcCategoryName == None:
                                gpcName = None

                            else:
                                gpcName = tradeItemClassification['gpcCategoryName']
                        else:
                            gpcName = None

                        if 'additionalTradeItemClassifications' in tradeItemClassification:
                            additionalTradeItemClassifications = tradeItemClassification['additionalTradeItemClassifications']
                            additionalTradeItemClassifications = additionalTradeItemClassifications[0]
                            if 'additionalTradeItemClassificationSystemCode' in additionalTradeItemClassifications:
                                additionalTradeItemClassificationSystemCode = additionalTradeItemClassifications['additionalTradeItemClassificationSystemCode']
                                if additionalTradeItemClassificationSystemCode == [] or additionalTradeItemClassificationSystemCode == None:
                                    ncmCode = None
                                else:
                                    ncmCode = additionalTradeItemClassifications['additionalTradeItemClassificationSystemCode']
                            else:
                                ncmCode = None

                            if 'additionalTradeItemClassificationCodeValue' in additionalTradeItemClassifications:
                                additionalTradeItemClassificationCodeValue = additionalTradeItemClassifications['additionalTradeItemClassificationCodeValue']
                                if additionalTradeItemClassificationCodeValue == [] or additionalTradeItemClassificationCodeValue == None:
                                    ncmValue = None
                                else:
                                    ncmValue = additionalTradeItemClassifications['additionalTradeItemClassificationCodeValue']
                                    ncmValue = ncmValue.replace('.','')
                            else:
                                ncmValue = None
                        else:
                            additionalTradeItemClassifications = None

                except:
                    tradeItemClassification = None
                    gpcCode = None
                    gpcName = None
                    additionalTradeItemClassifications = None
                    ncmCode = None
                    ncmValue = None


                tradeItemDescription = str(str(tradeItemDescription).replace("'", ''))
                additTradeItemDescription = str(str(additTradeItemDescription).replace("'", ''))
                print(additTradeItemDescription)
                childTradeItems = str(str(childTradeItems).replace("'", ''))
                referencedFileInformations = str(str(referencedFileInformations).replace("'", ''))
                uniformResourceIdentifier = str(str(uniformResourceIdentifier).replace("'", ''))
                contentDescription = str(str(contentDescription).replace("'", ''))
                fileName = str(str(fileName).replace("'", ''))
                referencedFileTypeCode = str(str(referencedFileTypeCode).replace("'", ''))
                featuredFile = str(str(featuredFile).replace("'", ''))
                gtinStatusCode = str(str(gtinStatusCode).replace("'", ''))
                brandName = str(str(brandName).replace("'", ''))
                languageCode = str(str(languageCode).replace("'", ''))
                measurementUnitCode = str(str(measurementUnitCode).replace("'", ''))
                measurementUnitCode_1 = str(str(measurementUnitCode_1).replace("'", ''))
                valor = str(str(valor).replace("'", ''))
                originalValue = str(str(originalValue).replace("'", ''))
                netvalue = str(str(netvalue).replace("'", ''))
                depth_value = str(str(depth_value).replace("'", ''))
                depth_measurementUnitCode = str(str(depth_measurementUnitCode).replace("'", ''))
                height_value = str(str(height_value).replace("'", ''))
                height_measurementUnitCode = str(str(height_measurementUnitCode).replace("'", ''))
                netContent_value = str(str(netContent_value).replace("'", ''))
                netContent_measurementUnitCode = str(str(netContent_measurementUnitCode).replace("'", ''))
                width_value = str(str(width_value).replace("'", ''))
                width_measurementUnitCode = str(str(width_measurementUnitCode).replace("'", ''))
                tradeItemClassification = str(str(tradeItemClassification).replace("'", ''))
                gpcCode = str(str(gpcCode).replace("'", ''))
                gpcName = str(str(gpcName).replace("'", ''))
                additionalTradeItemClassifications = str(str(additionalTradeItemClassifications).replace("'", ''))
                ncmCode = str(str(ncmCode).replace("'", ''))
                ncmValue = str(str(ncmValue).replace("'", ''))

        except:
            print('erro')

        referencedFileInformations = None
        referencedFileInformations = str(str(referencedFileInformations).replace("'", ''))
        tradeItemWeight = str(str(tradeItemWeight).replace("'", ''))
        tradeItemClassification = str(str(tradeItemClassification).replace("'", ''))
        tradeItemMeasurements = str(str(tradeItemMeasurements).replace("'", ''))
        depthAll = str(str(depthAll).replace("'", ''))
        height = str(str(height).replace("'", ''))
        netContent = str(str(netContent).replace("'", ''))
        width = str(str(width).replace("'", ''))
        tradeItemClassification = str(str(tradeItemClassification).replace("'", ''))

        if gtin != None:
            gtin = str(gtin)
            cursor = connection.cursor()  # cria um cursor
            cursor.execute("SELECT * from gs1_dados where gtin =" + gtin)  # consulta sql
            result = cursor.fetchone()  # busca o resultado da consulta
            gt = result

            gtin = int(gtin)



            '''Testa se o gtin já existe no banco. Se não existe, insere.'''

            if result == None:

                cursor.execute("SELECT * from gs1_dados order by id_gs1 desc")
                id_result = cursor.fetchone()
                id_gs1_in = id_result[0]
                id_gs1 = id_gs1_in + 1

                sql = 'insert into gs1_dados (featuredFile,width_measurementUnitCode,width_value,netContent_measurementUnitCode,netContent_value,netContent,height_measurementUnitCode,height_value,depth_measurementUnitCode,depth_value,depthAll,measurementUnitCode_1,netvalue,originalValue,valor,measurementUnitCode,languageCode,brandName,gtinStatusCode,referencedFileTypeCode,fileName,referencedFileInformations,gs1TradeItemIdentificationKey,uniformResourceIdentifier,height,width,tradeItemWeight,id_gs1,  gtin, fixedLengthGtin,  tradeItemDescription,  additTradeItemDescription, childTradeItems, contentDescription, tradeItemMeasurements,tradeItemClassification, gpcCode, gpcName, ncmCode, ncmValue ) values (:featuredFile,:width_measurementUnitCode,:width_value,:netContent_measurementUnitCode,:netContent_value,:netContent,:height_measurementUnitCode,:height_value,:depth_measurementUnitCode,:depth_value,:depthAll,:measurementUnitCode_1,:netvalue,:originalValue,:valor,:measurementUnitCode,:languageCode,:brandName,:gtinStatusCode,:referencedFileTypeCode,:fileName,:referencedFileInformations,:gs1TradeItemIdentificationKey,:uniformResourceIdentifier,:height,:width,:tradeItemWeight,:id_gs1,:gtin,:fixedLengthGtin,:tradeItemDescription,:additTradeItemDescription,:childTradeItems,:contentDescription,:tradeItemMeasurements,:tradeItemClassification,:gpcCode,:gpcName,:ncmCode,:ncmValue )'
                val = [featuredFile,width_measurementUnitCode,width_value,netContent_measurementUnitCode,netContent_value,netContent,height_measurementUnitCode,height_value,depth_measurementUnitCode,depth_value,depthAll,measurementUnitCode_1,netvalue,originalValue,valor,measurementUnitCode,languageCode,brandName,gtinStatusCode,referencedFileTypeCode,fileName,referencedFileInformations,gs1TradeItemIdentificationKey,uniformResourceIdentifier,height,width,tradeItemWeight, id_gs1,  gtin, fixedLengthGtin,  tradeItemDescription,  additTradeItemDescription, childTradeItems, contentDescription, tradeItemMeasurements,tradeItemClassification, gpcCode, gpcName, ncmCode, ncmValue ]
                cursor.execute(sql, val)
                cursor.execute("commit")

                print('Arquivo ' + arq + ' inserido no Banco de dados.')
            else:
                print(str(result[2]) + ' - GTIN já existe no banco!')
                print('_______')



        else:
            print('O arquivo não possui numero GTIN!')
