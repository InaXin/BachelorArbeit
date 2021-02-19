import pandas as pd

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
#htmlExcel_to_subExcel('Daten_Html/SubProductCategoryHtml.xlsx',30,'SubProductCategory')
#htmlExcel_to_subExcel('Daten/AllProductCategoryHtmlDropDuplicates.xlsx',100,'ProductCategory')

def productExcel_to_subExcel(excel_path:str,n:int):
    data = pd.read_excel(excel_path)
    long=data.count()[0]
    row = int(n)
    data['Produkt_ID']=data['Produkt_ID'].astype(str)
    if long % row == 0:
        n=int(long/row)
    else:
        n=int(long/row)+1
    for i in range(n):
        x = data[i*row:(i+1)*row]
        x.to_excel("%s(%s).xlsx" % (excel_path[:-5],str(i+1)),index=False)

#productExcel_to_subExcel('Daten/Json((2.-last)Handys&SmartphonesProductsInfo)ToExcel.xlsx',720)