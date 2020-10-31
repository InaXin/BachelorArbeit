import pandas as pd
excel_html = pd.ExcelFile('IdealoProductCategoryHtml.xlsx')
dataframe_html = excel_html.parse(excel_html.sheet_names[0])
n = 20
for i in range(0,len(dataframe_html['ProductCategory']),n):
    sub_dataframe_html = pd.DataFrame(columns=['ProductCategory'])
    temp_series = dataframe_html['ProductCategory'][i:i+n]
    #print('temp_series',temp_series,type(temp_series))
    dict_temp = dict()
    for temp_html in temp_series:
        dict_temp['ProductCategory'] = temp_html
        sub_dataframe_html = sub_dataframe_html.append(dict_temp,ignore_index=True)
    dict_temp.clear()
    print('sub_dataframe_html',sub_dataframe_html.shape)
    sub_dataframe_html.to_excel('SubHtmlExcel%s-%s.xlsx'%((i+1),(i+len(temp_series))),index=False)