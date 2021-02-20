from fbprophet import Prophet
from fbprophet.plot import plot_forecast_component
import pandas as pd
import matplotlib.pyplot as plt

class ProphetModel:

    #=================================function for plotting the predition===============================================
    def prediction_prophet(x,y,category_name,sainsonalitaetW:bool, saisonalitaetM:bool,saisonalitaetY:bool, gesetzlicheFeiertag:bool, sondereffekt:int, predict_period:int):
        plt.plot(x, y, marker='x')
        plt.title("Durchschnittliche Preisentwicklung von Kategorie '%s'" % category_name)
        plt.xlabel("Datum")
        plt.ylabel("durchschnittliche Produktpreise (€)")
        plt.grid()
        plt.tight_layout()

        dict_price = {"ds":x,"y":y}
        dataframe_avg_price = pd.DataFrame(dict_price)

        Preisaenderung_in_einer_Woche_ab_Ankuendigung_von_erstem_Lockdown = pd.DataFrame({
            'holiday': 'Preisaenderung_in_einer_Woche_ab_Ankuendigung_von_erstem_Lockdown',
            'ds': pd.to_datetime(
                ['2020-03-13'
                 ]),
            'lower_window': 0,
            'upper_window': 6,
        })

        Preisaenderung_in_einer_Woche_ab_Aufhebung_von_erstem_Lockdown = pd.DataFrame({
            'holiday': 'Preisaenderung_in_einer_Woche_ab_Aufhebung_von_erstem_Lockdown',
            'ds': pd.to_datetime(
                ['2020-4-27'
                 ]),
            'lower_window': 0,
            'upper_window': 6,
        })

        Preisaenderung_in_einer_Woche_Ankuendigung_Teil_Lockdown = pd.DataFrame({
            'holiday': 'Preisaenderung_in_einer_Woche_Ankuendigung_Teil_Lockdown',
            'ds': pd.to_datetime(
                ['2020-10-28'
                 ]),
            'lower_window': 0,
            'upper_window': 8,
        })

        Preisaenderung_in_amazon_prime_day = pd.DataFrame({
            'holiday': 'Preisaenderung_in_amazon_prime_day',
            'ds': pd.to_datetime(['2020-10-13', '2020-10-14']),
            'lower_window': -3,
            'upper_window': 3,
        })

        Preisaenderung_in_black_friday = pd.DataFrame({
            'holiday': 'Preisaenderung_in_black_friday',
            'ds': pd.to_datetime(['2020-11-27']),
            'lower_window': -3,
            'upper_window': 4,
        })

        Preisaenderung_in_singles_day = pd.DataFrame({
            'holiday': 'Preisaenderung_in_singles_day',
            'ds': pd.to_datetime(['2020-11-11']),
            'lower_window': -2,
            'upper_window': 2,
        })

        ### Sondereffekte
        if sondereffekt == 1:
            #corona
            holiday = pd.concat((Preisaenderung_in_einer_Woche_ab_Ankuendigung_von_erstem_Lockdown,
                                Preisaenderung_in_einer_Woche_ab_Aufhebung_von_erstem_Lockdown,
                                Preisaenderung_in_einer_Woche_Ankuendigung_Teil_Lockdown))
        elif sondereffekt == 2:
            #werbeaktion
            holiday = pd.concat((Preisaenderung_in_amazon_prime_day,
                                       Preisaenderung_in_black_friday,
                                       Preisaenderung_in_singles_day))
        elif sondereffekt == 3:
            #coronaAndWerbeaktion
            holiday = pd.concat((Preisaenderung_in_einer_Woche_ab_Ankuendigung_von_erstem_Lockdown,
                                           Preisaenderung_in_einer_Woche_ab_Aufhebung_von_erstem_Lockdown,
                                           Preisaenderung_in_einer_Woche_Ankuendigung_Teil_Lockdown,
                                           Preisaenderung_in_amazon_prime_day,
                                           Preisaenderung_in_black_friday,
                                           Preisaenderung_in_singles_day
                                           ))

        ###Model fit
        if sondereffekt == 0:
            m = Prophet(weekly_seasonality = False)
        else:
            m = Prophet(holidays= holiday,weekly_seasonality = False)

        #Saisonalitäten
        if sainsonalitaetW == True:
            m.add_seasonality(name = 'weekly',period = 7, fourier_order = 3)
        if saisonalitaetM == True:
            m.add_seasonality(name ='monthly', period=30.5, fourier_order=5)
        if saisonalitaetY == True:
            m.add_seasonality(name ='yearly', period=365.25, fourier_order=10)


        #gesetztliche Feiertage
        if gesetzlicheFeiertag == True:
            m.add_country_holidays(country_name='DE')


        m.fit(dataframe_avg_price)

        ###Predict
        future = m.make_future_dataframe(periods=predict_period)
        #print("future", future.tail())

        forecast = m.predict(future)
        #forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

        ###Plot results
        m.plot(forecast)

        m.plot_components(forecast)

        if sondereffekt == 1:
            #corona
            plot_forecast_component(m, forecast, 'Preisaenderung_in_einer_Woche_ab_Ankuendigung_von_erstem_Lockdown')

            plot_forecast_component(m, forecast, 'Preisaenderung_in_einer_Woche_ab_Aufhebung_von_erstem_Lockdown')

            plot_forecast_component(m, forecast, 'Preisaenderung_in_einer_Woche_Ankuendigung_Teil_Lockdown')

        if sondereffekt == 2:
            #werbeaktion
            plot_forecast_component(m, forecast, 'Preisaenderung_in_black_friday')

            plot_forecast_component(m, forecast, 'Preisaenderung_in_amazon_prime_day')

            plot_forecast_component(m, forecast, 'Preisaenderung_in_singles_day')

        if sondereffekt == 3:
            #coronaAndWerbeaktion
            plot_forecast_component(m, forecast, 'Preisaenderung_in_einer_Woche_ab_Ankuendigung_von_erstem_Lockdown')

            plot_forecast_component(m, forecast, 'Preisaenderung_in_einer_Woche_ab_Aufhebung_von_erstem_Lockdown')

            plot_forecast_component(m, forecast, 'Preisaenderung_in_einer_Woche_Ankuendigung_Teil_Lockdown')

            plot_forecast_component(m, forecast, 'Preisaenderung_in_black_friday')

            plot_forecast_component(m, forecast, 'Preisaenderung_in_amazon_prime_day')

            plot_forecast_component(m, forecast, 'Preisaenderung_in_singles_day')

        plt.show()

