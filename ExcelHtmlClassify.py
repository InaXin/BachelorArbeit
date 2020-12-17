import pandas as pd

excel_html = pd.ExcelFile('Daten_Html/IdealoProductCategoryHtmlDropDuplicates.xlsx')
dataframe_html = excel_html.parse(excel_html.sheet_names[0])

productCategory_dataframe_html = pd.DataFrame(columns=['ProductCategory'])
subProductCategory_dataframe_html = pd.DataFrame(columns=['SubProductCategory'])
travel_dataframe_html = pd.DataFrame(columns=['Plane&HotelHtml'])

dict_temp = dict()
for current_html in dataframe_html['ProductCategory']:
    if "SubProductCategory" in current_html:
        dict_temp['SubProductCategory'] = current_html
        subProductCategory_dataframe_html = subProductCategory_dataframe_html.append(dict_temp,ignore_index=True)
        print('subProductCategory',subProductCategory_dataframe_html)
        dict_temp.clear()
    elif "ProductCategory" in current_html:
        dict_temp['ProductCategory'] = current_html
        productCategory_dataframe_html = productCategory_dataframe_html.append(dict_temp,ignore_index=True)
        print('productCategory',productCategory_dataframe_html)
        dict_temp.clear()
    else:
        dict_temp['Plane&HotelHtml'] = current_html
        travel_dataframe_html = travel_dataframe_html.append(dict_temp,ignore_index=True)
        print('travel',travel_dataframe_html)
        dict_temp.clear()

subProductCategory_dataframe_html.to_excel('Daten_Html/SubProductCategoryHtml.xlsx', index=False)
productCategory_dataframe_html.to_excel('Daten_Html/ProductCategoryHtml.xlsx',index = False)
travel_dataframe_html.to_excel('Daten_Html/Plane&HotelHtml.xlsx',index = False)


