import pandas as pd
import json
import os


excel_product = pd.ExcelFile('Daten/IdealoKategorien.xlsx')
dataframe_product = excel_product.parse(excel_product.sheet_names[0])
#print(dataframe_product)


###################all category number########################################################################
category_id = 1
dict_category_number = dict()
for category_name in dataframe_product['Kategorie 1']:
    if category_name is not None and category_name not in dict_category_number.keys():
        dict_category_number[category_name] = category_id
        category_id = category_id + 1
for category_name in dataframe_product['Kategorie 2']:
    if category_name is not None and category_name not in dict_category_number.keys():
        dict_category_number[category_name] = category_id
        category_id = category_id + 1
for category_name in dataframe_product['Kategorie 3']:
    if category_name is not None and category_name not in dict_category_number.keys():
        dict_category_number[category_name] = category_id
        category_id = category_id + 1
for category_name in dataframe_product['Kategorie 4']:
    if category_name is not None and category_name not in dict_category_number.keys():
        dict_category_number[category_name] = category_id
        category_id = category_id + 1

##################category dataframe###########################################################################
dataframe_category = pd.DataFrame(columns=['category_id', 'category_name', 'super_category_id'])
dict_current = dict()
for curent_category_name in dict_category_number.keys():
    if curent_category_name in dataframe_product['Kategorie 1'].values:
        dict_current['category_id'] = dict_category_number[curent_category_name]
        dict_current['category_name'] = curent_category_name
        dataframe_category = dataframe_category.append(dict_current, ignore_index=True)
        dict_current.clear()
        continue
    if curent_category_name in dataframe_product['Kategorie 2'].values:
        dict_current['category_id'] = dict_category_number[curent_category_name]
        dict_current['category_name'] = curent_category_name
        dict_current['super_category_id'] = dict_category_number[dataframe_product[dataframe_product['Kategorie 2'] == curent_category_name]['Kategorie 1'].values[0]]
        dataframe_category = dataframe_category.append(dict_current, ignore_index=True)
        dict_current.clear()
        continue
    if curent_category_name in dataframe_product['Kategorie 3'].values:
        dict_current['category_id'] = dict_category_number[curent_category_name]
        dict_current['category_name'] = curent_category_name
        dict_current['super_category_id'] = dict_category_number[dataframe_product[dataframe_product['Kategorie 3'] == curent_category_name]['Kategorie 2'].values[0]]
        dataframe_category = dataframe_category.append(dict_current, ignore_index=True)
        dict_current.clear()
        continue
    if curent_category_name in dataframe_product['Kategorie 4'].values:
        dict_current['category_id'] = dict_category_number[curent_category_name]
        dict_current['category_name'] = curent_category_name
        dict_current['super_category_id'] = dict_category_number[dataframe_product[dataframe_product['Kategorie 4'] == curent_category_name]['Kategorie 3'].values[0]]
        dataframe_category = dataframe_category.append(dict_current, ignore_index=True)
        dict_current.clear()
        continue

###############################product dataframe######################################################################
dataframe_product_category = pd.DataFrame(columns=['product_id', 'product_name', 'category_id'])
for row_index in range(len(dataframe_product)):
    dict_current['product_id'] = dataframe_product['Produkt_ID'][row_index]
    dict_current['product_name'] = dataframe_product['Produkt_Name'][row_index]
    category_id = 0
    if pd.notna(dataframe_product['Kategorie 1'][row_index]):
        category_id = dict_category_number[dataframe_product['Kategorie 1'][row_index]]
    if pd.notna(dataframe_product['Kategorie 2'][row_index]):
        category_id = dict_category_number[dataframe_product['Kategorie 2'][row_index]]
    if pd.notna(dataframe_product['Kategorie 3'][row_index]):
        category_id = dict_category_number[dataframe_product['Kategorie 3'][row_index]]
    if pd.notna(dataframe_product['Kategorie 4'][row_index]):
        category_id = dict_category_number[dataframe_product['Kategorie 4'][row_index]]
    dict_current['category_id'] = category_id
    dataframe_product_category = dataframe_product_category.append(dict_current, ignore_index=True)
    dict_current.clear()

#####################################product url#############################################################
for i in range(len(dataframe_product['Produkt_ID'])):
    temp_url = 'https://www.idealo.de/offerpage/pricechart/api/{}?period=P1Y'.format(dataframe_product['Produkt_ID'][i])
    with os.popen('curl -k {}'.format(temp_url)) as p:
        result = p.read()
        result_dict = json.loads(result)
