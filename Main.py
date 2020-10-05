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
#DatenPlotModel.plotAllProducts(resultAllProducts[0],resultAllProducts[1])

######plot the trend of different Category in one graph
resultTopCategories = databaseProcessor.get_top_category()
#DatenPlotModel.plotAllCategory(resultTopCategories)

######plot the trend of each category
for key,value in resultTopCategories.items():
    result = databaseProcessor.get_average_eachCategory(key)
    #DatenPlotModel.plotEachCategory(result[0], result[1],value)

######plot the prediction of all products using LSTM
dict_price = {"date":resultAllProducts[0],"avg_price":resultAllProducts[1]}
#LstmModel.pricePredictLSTM(dict_price, 'Alle Produkte')

######plot the prediction of all products using Prophet
#ProphetModel.predictionAllProducts(resultAllProducts[0],resultAllProducts[1])

######plot the prediction of each category using Prophet
for key,value in resultTopCategories.items():
    result = databaseProcessor.get_average_eachCategory(key)
    ProphetModel.predictionEachCategory(result[0],result[1],value)





