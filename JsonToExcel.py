import json
import pandas as pd

json_path = 'Daten_Json_Clean/(2.-last)Handys&SmartphonesProductsInfo.json'

with open(json_path) as f:
    data = json.load(f)

excel_path = 'Daten/Json(%s)ToExcel.xlsx'% json_path[17:-5]
#print(excel_path)

dataframe_temp = pd.DataFrame(columns=['Produkt_ID','Produkt_Name','Kategorie 1','Kategorie 2','Kategorie 3','Kategorie 4','Kategorie 5','Kategorie 6','Kategorie 7','Link'])
for current_result in data:
    for list_temp in current_result:
        dict_temp = dict()
        for item in list_temp:
            current_length = len(item)
            dict_temp['Produkt_ID'] = item[0]
            dict_temp['Produkt_Name'] = item[1]
            dict_temp['Link'] = item[current_length-1]
            index = 2
            for index in range(current_length-1):
                dict_temp[dataframe_temp.columns[index]] = item[index]
            dataframe_temp = dataframe_temp.append(dict_temp,ignore_index=True)
            dict_temp.clear()
        dataframe_temp.to_excel(excel_path,index = False)