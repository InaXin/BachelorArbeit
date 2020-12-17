import json
import os
class DataCleaning:

    def __init__(self,json_path:str):
        self.json_path = json_path

    def drop_abnormal_data(self):
        clean_result = []
        data_result = []
        file_name = self.json_path
        file_name_after_clean = 'Daten_Json_Clean/ProductsInfo(2001-2011).json'
        with open(file_name, mode='r') as f:
            data = json.load(f)
            for current_result in data:
                for temp_result in current_result:
                    remove_list = []
                    for current_list in temp_result:
                        if "IDNoFound" in current_list:
                            remove_list.append(current_list)
                    for i in remove_list:
                        temp_result.remove(i)
                for j in current_result:
                    if len(j):
                        clean_result.append(j)
                    else:
                        pass
                data_result.append(clean_result)

        #os.remove(file_name)
        with open(file_name_after_clean, mode='w', encoding='utf-8') as f:
            json.dump(data_result, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    dataCleaning = DataCleaning('Daten_Json(09.Nov-11.Nov)/AllProductCategoryHtmlDropDuplicates(2001-2011)ToProductsInfo.json')
    dataCleaning.drop_abnormal_data()