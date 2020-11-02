import LstmModel
import DatenPlotModel
from LstmModel import *
from DatenPlotModel import *
from ProphetModel import *
from DataFormat import *
from DatabaseProcessor import *

######connect database
databaseProcessor = DatabaseProcesser("localhost","root","6857","IdealoPreis")
######plot the trend of all products
result_all_products = databaseProcessor.get_average_price_all_date()
#print(result_all_products[0],result_all_products[1])
#DatenPlotModel.plot_all_products(result_all_products[0],result_all_products[1])

######plot the trend of different Category in one graph
result_top_categories = databaseProcessor.get_top_category()
#DatenPlotModel.plot_all_categories(result_top_categories)

######plot the trend of each category
for key,value in result_top_categories.items():
    result = databaseProcessor.get_average_eachCategory(key)
    DatenPlotModel.plot_each_category(result[0], result[1],value)

######plot the prediction of all products using LSTM
dict_price = {"date":result_all_products[0],"avg_price":result_all_products[1]}
#LstmModel.price_prediction_LSTM(dict_price, 'Alle Produkte')

######plot the prediction of all products using Prophet
#ProphetModel.prediction_all_products(result_all_products[0],result_all_products[1])

######plot the prediction of each category using Prophet
for key,value in result_top_categories.items():
    result = databaseProcessor.get_average_eachCategory(key)
    #ProphetModel.prediction_each_category(result[0],result[1],value)

databaseProcessor.close()



