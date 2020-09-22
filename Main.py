import DatabaseProcessor
import DatenPredictionModel
import DatenPlotModel
from DatabaseProcessor import *
from DatenPredictionModel import *
from DatenPlotModel import *

databaseProcessor = DatabaseProcessor.DatabaseProcesser()
databaseProcessor.db = pymysql.connect("localhost","root","6857","IdealoPreis")

###plot the trend of all products
resultAllProducts = databaseProcessor.get_average_price_allDate()
DatenPlotModel.plotAllProducts(resultAllProducts[0],resultAllProducts[1])

###plotthe trend of different Category in one graph
resultTopCategories = databaseProcessor.get_top_category()
DatenPlotModel.plotAllCategory(resultTopCategories)

###plot the trend of each Category
for key,value in resultTopCategories.items():
    result = databaseProcessor.get_average_eachCategory(key)
    DatenPlotModel.plotEachCategory(result[0], result[1],value)

###plot the prediction of all products using LSTM
dict_price = {"date":resultAllProducts[0],"avg_price":resultAllProducts[1]}
DatenPredictionModel.pricePredictLSTM(dict_price,'Alle Produkte')




