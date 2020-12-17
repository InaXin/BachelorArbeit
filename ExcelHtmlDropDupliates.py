import pandas as pd

#for excel only one culumn
def excel_drop_duplicates(excel_path:str, culumn_name:str):
    excel_html = pd.ExcelFile(excel_path)
    dataframe_html = excel_html.parse(excel_html.sheet_names[0])
    dataframe_html = dataframe_html.drop_duplicates(subset = culumn_name,keep ='first',inplace = False)
    dataframe_html.to_excel('%sDropDuplicates.xlsx'%excel_path[:-5],index=False)

excel_drop_duplicates('Daten_Html/AllProductCategoryHtml.xlsx','ProductCategory')