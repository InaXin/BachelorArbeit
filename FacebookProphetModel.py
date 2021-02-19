from fbprophet import Prophet
from fbprophet.plot import plot_forecast_component
import pandas as pd
import matplotlib.pyplot as plt

class ProphetModel:

    #=================================function for plotting the predition===============================================
    def prediction_prophet(x,y):
        dict_price = {"ds":x,"y":y}
        dataframe_avg_price = pd.DataFrame(dict_price)

        Preisänderung_in_einer_Woche_ab_Ankündigung_von_erstem_Lockdown = pd.DataFrame({
            'holiday': 'Preisänderung_in_einer_Woche_ab_Ankündigung_von_erstem_Lockdown',
            'ds': pd.to_datetime(
                ['2020-03-13'
                 ]),
            'lower_window': 0,
            'upper_window': 6,
        })

        Preisänderung_in_einer_Woche_ab_Aufhebung_von_erstem_Lockdown = pd.DataFrame({
            'holiday': 'Preisänderung_in_einer_Woche_ab_Aufhebung_von_erstem_Lockdown',
            'ds': pd.to_datetime(
                ['2020-4-27'
                 ]),
            'lower_window': 0,
            'upper_window': 6,
        })

        Preisänderung_in_einer_Woche_Ankündigung_Teil_Lockdown = pd.DataFrame({
            'holiday': 'Preisänderung_in_einer_Woche_Ankündigung_Teil_Lockdown',
            'ds': pd.to_datetime(
                ['2020-10-28'
                 ]),
            'lower_window': 0,
            'upper_window': 8,
        })

        Preisänderung_in_amazon_prime_day = pd.DataFrame({
            'holiday': 'Preisänderung_in_amazon_prime_day',
            'ds': pd.to_datetime(['2020-10-13', '2020-10-14']),
            'lower_window': -3,
            'upper_window': 3,
        })

        Preisänderung_in_black_friday = pd.DataFrame({
            'holiday': 'Preisänderung_in_black_friday',
            'ds': pd.to_datetime(['2020-11-27']),
            'lower_window': -3,
            'upper_window': 4,
        })

        Preisänderung_in_singles_day = pd.DataFrame({
            'holiday': 'Preisänderung_in_singles_day',
            'ds': pd.to_datetime(['2020-11-11']),
            'lower_window': -2,
            'upper_window': 2,
        })

        corona = pd.concat((Preisänderung_in_einer_Woche_ab_Ankündigung_von_erstem_Lockdown,
                            Preisänderung_in_einer_Woche_ab_Aufhebung_von_erstem_Lockdown,
                            Preisänderung_in_einer_Woche_Ankündigung_Teil_Lockdown))

        werbeaktion = pd.concat((Preisänderung_in_amazon_prime_day,
                                   Preisänderung_in_black_friday,
                                   Preisänderung_in_singles_day))

        coronaAndWerbeaktion = pd.concat((Preisänderung_in_einer_Woche_ab_Ankündigung_von_erstem_Lockdown,
                                       Preisänderung_in_einer_Woche_ab_Aufhebung_von_erstem_Lockdown,
                                       Preisänderung_in_einer_Woche_Ankündigung_Teil_Lockdown,
                                       Preisänderung_in_amazon_prime_day,
                                       Preisänderung_in_black_friday,
                                       Preisänderung_in_singles_day
                                       ))

        # =================================einstellbare Parameter=========================================
        ###Model fit
        m = Prophet(holidays= corona, weekly_seasonality = False)
        #m.add_seasonality(name='monthly', period=30.5, fourier_order=5)
        m.add_seasonality(name='yearly', period=365.25, fourier_order=10)
        # m.add_seasonality(name ='quarterly', period=365.25/4, fourier_order = 5)
        # gesetztliche Feiertage
        m.add_country_holidays(country_name='DE')
        # =================================einstellbare Parameter=========================================


        m.fit(dataframe_avg_price)

        ###Predict
        future = m.make_future_dataframe(periods=365)
        #print("future", future.tail())

        forecast = m.predict(future)
        #forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

        ###Plot results
        m.plot(forecast)

        m.plot_components(forecast)


        ###corona
        plot_forecast_component(m, forecast, 'Preisänderung_in_einer_Woche_ab_Ankündigung_von_erstem_Lockdown')

        plot_forecast_component(m, forecast, 'Preisänderung_in_einer_Woche_ab_Aufhebung_von_erstem_Lockdown')

        plot_forecast_component(m, forecast, 'Preisänderung_in_einer_Woche_Ankündigung_Teil_Lockdown')



        # ###werbeaktion
        # plot_forecast_component(m, forecast, 'Preisänderung_in_black_friday')
        #
        # plot_forecast_component(m, forecast, 'Preisänderung_in_amazon_prime_day')
        #
        # plot_forecast_component(m, forecast, 'Preisänderung_in_singles_day')



        # ###coronaAndWerbeaktion
        # plot_forecast_component(m, forecast, 'Preisänderung_in_einer_Woche_ab_Ankündigung_von_erstem_Lockdown')
        #
        # plot_forecast_component(m, forecast, 'Preisänderung_in_einer_Woche_ab_Aufhebung_von_erstem_Lockdown')
        #
        # plot_forecast_component(m, forecast, 'Preisänderung_in_einer_Woche_Ankündigung_Teil_Lockdown')
        #
        # plot_forecast_component(m, forecast, 'Preisänderung_in_black_friday')
        #
        # plot_forecast_component(m, forecast, 'Preisänderung_in_amazon_prime_day')
        #
        # plot_forecast_component(m, forecast, 'Preisänderung_in_singles_day')


        plt.show()

