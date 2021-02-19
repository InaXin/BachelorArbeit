import LstmModel
import DatenPlotModel
from LstmModel import *
from DatenPlotModel import *
from FacebookProphetModel import *
from DataFormat import *
from DatabaseProcessor import *

#======================================einstellbare Parameter===========================================================
category_name = "Toilettenartikel"
start_date = "2020-02-11"
end_date = "2021-02-06"
#======================================connect database=================================================================
databaseProcessor = DatabaseProcesser("localhost","root","6857","IdealoPreis")

#=================================================Retrieve data from the database=======================================
result = databaseProcessor.get_average_price_byCategory_overTime(category_name,start_date,end_date)

#================================================Plot the price changes=================================================
DatenPlotModel.plot_category(result[0],result[1],category_name)

#===================================================Plot the analyse and prediction using Prophet=======================
ProphetModel.prediction_prophet(result[0],result[1])

#================================================Plot the Prediction using LSTM hier for test epochs = 200=========================================
dict_date_price = {"date":result[0],"avg_price":result[1]}
#LstmModel.prediction_LSTM(dict_date_price, category_name)

#===================================================datebase close=======================
databaseProcessor.close()



