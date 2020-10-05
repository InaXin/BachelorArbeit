import DatabaseProcessor
import LstmModel
import DatenPlotModel
from DatabaseProcessor import *
from LstmModel import *
from DatenPlotModel import *
from ProphetModel import *

######connect database
databaseProcessor = DatabaseProcessor.DatabaseProcesser()
databaseProcessor.db = pymysql.connect("localhost","root","6857","IdealoPreis")

######plot the trend of all products
resultAllProducts = databaseProcessor.get_average_price_allDate()
DatenPlotModel.plot_all_products(resultAllProducts[0],resultAllProducts[1])

######plot the trend of different Category in one graph
resultTopCategories = databaseProcessor.get_top_category()
DatenPlotModel.plot_all_categories(resultTopCategories)

######plot the trend of each category
for key,value in resultTopCategories.items():
    result = databaseProcessor.get_average_eachCategory(key)
    DatenPlotModel.plot_each_category(result[0], result[1],value)

######plot the prediction of all products using LSTM
dict_price = {"date":resultAllProducts[0],"avg_price":resultAllProducts[1]}
LstmModel.price_prediction_LSTM(dict_price, 'Alle Produkte')

######plot the prediction of all products using Prophet
ProphetModel.prediction_all_products(resultAllProducts[0],resultAllProducts[1])

######plot the prediction of each category using Prophet
for key,value in resultTopCategories.items():
    result = databaseProcessor.get_average_eachCategory(key)
    ProphetModel.prediction_each_category(result[0],result[1],value)





