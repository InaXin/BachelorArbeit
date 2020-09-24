import pandas as pd
from fbprophet import Prophet
import pymysql
import DatabaseProcessor
import pandas
import matplotlib.pyplot  as plt

databaseProcessor = DatabaseProcessor.DatabaseProcesser()
databaseProcessor.db = pymysql.connect("localhost","root","6857","IdealoPreis")

resultAllProducts = databaseProcessor.get_average_price_allDate()

dict_price = {"ds":resultAllProducts[0],"y":resultAllProducts[1]}
dataframe_avg_price = pd.DataFrame(dict_price)
print("dataframe_avg_price",dataframe_avg_price.head())

m = Prophet()
m.fit(dataframe_avg_price)

future = m.make_future_dataframe(periods=365)
print("future",future.tail())

forecast = m.predict(future)
print("forecast",forecast[['ds','yhat','yhat_lower','yhat_upper']].tail())

m.plot(forecast)
#m.plot_components(forecast)
plt.show()