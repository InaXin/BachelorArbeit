from LstmModel import *
from FacebookProphetModel import *
from DatabaseProcessor import *


#======================================setting parameters===========================================================
category_name = "Desinfektionsmittel"               ###aus CategoyListForTest.xlsx aussuchen
start_date = "2020-02-07"                           ### Format muss "YYYY-MM-DD". Kann auch leer sein. Wenn die start_date und end_date leer sind, werden alle Datums gezeigt.
end_date = "2021-02-06"                             ### Format muss "YYYY-MM-DD". Kann auch leer sein. Wenn die start_date und end_date leer sind, werden alle Datums gezeigt.
sasonalitaetWoche = False                           ### bool, Ob wöchentlicher Einfluss in Modell addiert wird.
sasonalitaetMonat = False                           ### bool, Ob monatlicher Einfluss in Modell addiert wird
sasonalitaetJahr = True                             ### bool, Ob jährlicher Einfluss in Modell addiert wird
gesetzlicheFeiertag = True                          ### bool, Ob die Einfüsse von gesetzicher Feiertag in Modell addiert werden
sonderEffekt = 1                                    ### int,  0: kein Sondereffekt 1:Corona, 2:Werbeaktion, 3:Corona und Werbeaktion
predict_period = 365                                ### int,  Zeitraum von Prognose

#======================================database connect=================================================================
databaseProcessor = DatabaseProcesser("localhost","root","6857","IdealoPreis")


#=================================================retrieve data from database=======================================
###Average price with a certain period
result = databaseProcessor.get_average_price_byCategory_period(category_name,start_date,end_date)

###Average price of all dates of selected category in database
#result = databaseProcessor.get_average_price_byCategory(category_name)


#===================================================analysis and forecast model Facebook Prophet=======================
ProphetModel.prediction_prophet(result[0],result[1], category_name,sasonalitaetWoche,sasonalitaetMonat,sasonalitaetJahr,gesetzlicheFeiertag,sonderEffekt,predict_period)


#================================================Forecast model Lstm for test epochs = 100=========================================
dict_date_price = {"date":result[0],"avg_price":result[1]}
#LstmModel.prediction_LSTM(dict_date_price, category_name)


#===================================================database close=======================
databaseProcessor.close()



