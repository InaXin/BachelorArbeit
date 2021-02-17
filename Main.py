import LstmModel
import DatenPlotModel
from LstmModel import *
from DatenPlotModel import *
from FacebookProphetModel import *
from DataFormat import *
from DatabaseProcessor import *

#======================================connect database=================================================================
databaseProcessor = DatabaseProcesser("localhost","root","6857","IdealoPreis")

#=================================================Retrieve data from the database=======================================
#result_toilettenartikel = databaseProcessor.get_average_price_toilettenartikel()

#result_desinfektionsmittel = databaseProcessor.get_average_price_desinfektionsmittel()

#result_handys = databaseProcessor.get_average_price_handys()

#================================================Plot the price changes=================================================
#toilettenartikel
#DatenPlotModel.plot_toilettenartikel(result_toilettenartikel[0],result_toilettenartikel[1])

#Desinfektionsmittel
#DatenPlotModel.plot_desinfektionsmittel(result_desinfektionsmittel[0],result_desinfektionsmittel[1])

#Handys
#DatenPlotModel.plot_handys(result_handys[0],result_handys[1])

#================================================Plot the Prediction using LSTM=========================================
######toilettenartikel
# dict_price = {"date":result_toilettenartikel[0],"avg_price":result_toilettenartikel[1]}
# LstmModel.prediction_LSTM(dict_price, 'Toilettenartikel')

#===================================================Plot the analyse and prediction using Prophet=======================
######Toilettenartikel
#ProphetModel.prediction_prophet(result_toilettenartikel[0],result_toilettenartikel[1])

######Desinfektionsmittel
#ProphetModel.prediction_prophet(result_desinfektionsmittel[0],result_desinfektionsmittel[1])

######Handys&Smartphones
#ProphetModel.prediction_prophet(result_handys[0],result_handys[1])

###database close
databaseProcessor.close()



