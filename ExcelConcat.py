import pandas as pd

file1 = 'Daten_Html/ProductCategoryHtml.xlsx'
file2 = 'Daten_Html/SubProductCategory(1-30)ToProductCategoryHtml.xlsx'
file3 = 'Daten_Html/SubProductCategory(31-60)ToProductCategoryHtml.xlsx'
file4 = 'Daten_Html/SubProductCategory(61-70)ToProductCategoryHtml.xlsx'
file = [file1, file2,file3,file4]
li = []
for current_file in file:
    li.append(pd.read_excel(current_file))
writer = pd.ExcelWriter('Daten_Html/AllProductCategoryHtml.xlsx')
pd.concat(li).to_excel(writer, 'Sheet1', index=False)

writer.save()