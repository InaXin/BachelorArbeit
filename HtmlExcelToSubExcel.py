import pandas as pd

#for excel only one column
# def htmlExcel_to_subExcel(excel_path:str,n:int,culumn_name:str):
#     excel_html = pd.ExcelFile(excel_path)
#     dataframe_html = excel_html.parse(excel_html.sheet_names[0])
#     n = n
#     for i in range(0, len(dataframe_html[culumn_name]), n):
#         sub_dataframe_html = pd.DataFrame(columns=[culumn_name])
#         temp_series = dataframe_html[culumn_name][i:i + n]
#         # print('temp_series',temp_series,type(temp_series))
#         dict_temp = dict()
#         for temp_html in temp_series:
#             dict_temp[culumn_name] = temp_html
#             sub_dataframe_html = sub_dataframe_html.append(dict_temp, ignore_index=True)
#         dict_temp.clear()
#         print('sub_dataframe_html', sub_dataframe_html.shape)
#         sub_dataframe_html.to_excel("%s(%s-%s).xlsx" % (excel_path[:-5],(i + 1), (i + len(temp_series))), index=False)

#htmlExcel_to_subExcel('Daten/AllProductCategoryHtmlDropDuplicates.xlsx',100,'ProductCategory')

def htmlExcel_to_subExcel(excel_path:str,n:int,culumn_name:str):
    excel_html = pd.ExcelFile(excel_path)
    dataframe_html = excel_html.parse(excel_html.sheet_names[0])
    n = n
    for i in range(0, len(dataframe_html[culumn_name]), n):
        sub_dataframe_html = pd.DataFrame(columns=[culumn_name])
        temp_series = dataframe_html[culumn_name][i:i + n]
        # print('temp_series',temp_series,type(temp_series))
        dict_temp = dict()
        for temp_html in temp_series:
            dict_temp[culumn_name] = temp_html
            sub_dataframe_html = sub_dataframe_html.append(dict_temp, ignore_index=True)
        dict_temp.clear()
        print('sub_dataframe_html', sub_dataframe_html.shape)
        sub_dataframe_html.to_excel("%s(%s-%s).xlsx" % (excel_path[:-5],(i + 1), (i + len(temp_series))), index=False)
#htmlExcel_to_subExcel('Daten/AllProductCategoryHtmlDropDuplicates.xlsx',100,'ProductCategory')

import pandas as pd
from pandas import DataFrame,Series
excel_path = "Daten/Json(ProductsInfo(1901-2000))ToExcel.xlsx"
data = pd.read_excel(excel_path)
long=data.count()[0]
row = int(1200)
data['Produkt_ID']=data['Produkt_ID'].astype(str) #excel表格超过15位就会变成文本形式，如果有超过18位的数字需要加上一句
if long % row == 0:
    n=int(long/row)
else:
    n=int(long/row)+1
for i in range(n):
    x = data[i*row:(i+1)*row]#最后一行无法除尽也没关系
    x.to_excel("%s(%s).xlsx" % (excel_path[:-5],str(i+1)),index=False)