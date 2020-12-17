import json

class DataChecking:

    def __init__(self,json_path):
        self.json_path = json_path

    def maxLenProduct(self):
        with open(self.json_path) as f:
            data = json.load(f)
            print('data',data)
            temp_list = []
            for current_result in data:
                print('len_current_result',len(current_result))
                #print('current_result',current_result)
                index = 1
                for temp_result in current_result:
                    #print(temp_result[0],temp_result[-1])
                    print("temp_result:",str(index)+")",temp_result)
                    print('len_temp_result',len(temp_result))
                    index = index + 1
                    temp_list1 = []
                    for current_product_list in temp_result:
                        len_current_product_list = len(current_product_list)
                        temp_list1.append(len_current_product_list)
                        if current_product_list[0] == "IDNoFound" or current_product_list[1] == "NameNoFound" or current_product_list[1] == '':

                            print("==============Abnormal Data=============",current_product_list)

                    max_len_current_product_list = max(temp_list1)
                    print('max_len_current_product_list', max_len_current_product_list)
                    temp_list.append(max_len_current_product_list)
            max_len = max(temp_list)
            max_index = temp_list.index(max_len)
            print('len_temp_list',len(temp_list))
            print('max_len',max_len)
            print("max_index",max_index)
            print(current_result[max_index])
            return max_len

if __name__ == '__main__':
    #dataChecking = DataChecking('Daten_Json(09.Nov-11.Nov)/AllProductCategoryHtmlDropDuplicates(1901-2000)ToProductsInfo.json')
    dataChecking = DataChecking('Daten_Json_Clean/ProductsInfo(401-500).json')
    dataChecking.maxLenProduct()