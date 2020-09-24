from fbprophet import Prophet
import pymysql
from fbprophet.plot import plot_forecast_component

import DatabaseProcessor
import pandas as pd
import matplotlib.pyplot as plt

databaseProcessor = DatabaseProcessor.DatabaseProcesser()
databaseProcessor.db = pymysql.connect("localhost","root","6857","IdealoPreis")

resultAllProducts = databaseProcessor.get_average_price_allDate()

dict_price = {"ds":resultAllProducts[0],"y":resultAllProducts[1]}
dataframe_avg_price = pd.DataFrame(dict_price)
# print("dataframe_avg_price",dataframe_avg_price.head())

m = Prophet()
m.fit(dataframe_avg_price)

future = m.make_future_dataframe(periods=150)
print("future",future.tail())

#forecast = m.predict(future)
#print("forecast",forecast[['ds','yhat','yhat_lower','yhat_upper']].tail())

corona_policy = pd.DataFrame({
 'holiday': 'corona_policy',
 'ds': pd.to_datetime(
 ['2020-01-27', '2020-03-22', '2020-04-20',
 ]),
 'lower_window': -3,
 'upper_window': 3,
})
events = corona_policy
m = Prophet(holidays=events)
m.add_country_holidays(country_name='DE')
#print("holidays_name",m.train_holiday_names)
forecast = m.fit(dataframe_avg_price).predict(future)
fig = m.plot_components(forecast)
fig.savefig('image/Events.svg')

fig = plot_forecast_component(m, forecast, 'corona_policy')
fig = plt.gcf()
fig.savefig('image/corona_policy.svg')
plt.show()

#m.plot(forecast)
#m.plot_components(forecast)
#plt.show()