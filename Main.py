import LstmModel
import DatenPlotModel
from LstmModel import *
from DatenPlotModel import *
from FacebookProphetModel import *
from DataFormat import *
from DatabaseProcessor import *


#======================================einstellbare Parameter===========================================================
category_name = "Desinfektionsmittel"   ###aus CategoyListForTest.xlsx aussuchen
start_date = "2020-02-11"               ### Format muss "YYYY-MM-DD"
end_date = "2021-02-06"                 ### Format muss "YYYY-MM-DD"
sasonalitaetWoche = False              ### bool, True: wöchentlicher Einfluss in Modell addieren
sasonalitaetMonat = False              ### bool, True: monatlicher Einfluss in Modell addieren
sasonalitaetJahr = False               ### bool, Ture: jährlicher Einfluss in Modell addieren
gesetzlicheFeiertag = False            ### bool, True: die Einfüsse von gesetzicher Feiertag in Modell addieren
sonderEffekt = 3                       ### int,  0: kein Sondereffekt 1:corona, 2:werbeaktion, 3:corona und werbeaktion
predict_period = 0                     ### int,  Prediction Zeitraum(0-365 Tagen)

#======================================connect database=================================================================
databaseProcessor = DatabaseProcesser("localhost","root","6857","IdealoPreis")

#=================================================Retrieve data from the database=======================================
result = databaseProcessor.get_average_price_byCategory_overTime(category_name,start_date,end_date)

#================================================Plot the price changes=================================================
#DatenPlotModel.plot_category(result[0],result[1],category_name)

#===================================================Plot the analyse and prediction using Prophet=======================
ProphetModel.prediction_prophet(result[0],result[1], sasonalitaetWoche,sasonalitaetMonat,sasonalitaetJahr,gesetzlicheFeiertag,sonderEffekt,predict_period)

#================================================Plot the Prediction using LSTM hier for test epochs = 200=========================================
dict_date_price = {"date":result[0],"avg_price":result[1]}
#LstmModel.prediction_LSTM(dict_date_price, category_name)

#===================================================datebase close=======================
databaseProcessor.close()



