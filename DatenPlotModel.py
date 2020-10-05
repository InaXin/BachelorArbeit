import matplotlib.pyplot as plt
import pandas as pd
import pymysql
import DatabaseProcessor


class DatenPlotModel:

    #############function for plotting the trend of all products##########################################
    def plot_all_products(x,y):
        fig = plt.figure(figsize=(12,6))
        plt.plot(x,y)
        plt.vlines(pd.to_datetime('2020-01-27'), min(y), max(y), colors="r", linestyles="-.",linewidth=3,
                   label = "Erste Erkrankung in Deutschland(27.01.20)")
        plt.vlines(pd.to_datetime('2020-03-22'), min(y), max(y), colors="g", linestyles="-.",linewidth=3,
                   label= "Lock Down(22.03.20)"),
        plt.vlines(pd.to_datetime('2020-04-20'), min(y), max(y), colors="b", linestyles="-.",linewidth=3,
                   label= "Erste Lockerung(20.04.20)")

        plt.title("Durchschnittliche Preisentwicklung von allen Produkten(von Sep. 2019 bis Sep. 2020)",fontsize=16)
        plt.xlabel("Datum")
        plt.ylabel("durchschnittliche Produktpreise (€)")

        plt.legend()
        plt.grid()
        plt.tight_layout()
        fig.savefig('image/AllProducts.svg')
        plt.show()

    ###################function for plotting the trend of each Category #####################################
    def plot_each_category(x, y, categoryName):
        fig = plt.figure(figsize=(12, 6))
        plt.plot(x, y)
        try:
            plt.vlines(pd.to_datetime('2020-01-27'), min(y), max(y), colors="r", linestyles="-.",
                       linewidth=3,
                       label="Erste Erkrankung in Deutschland(27.01.20)")
            plt.vlines(pd.to_datetime('2020-03-22'), min(y), max(y), colors="g", linestyles="-.",
                       linewidth=3,
                       label="Lock Down(22.03.20)"),
            plt.vlines(pd.to_datetime('2020-04-20'), min(y), max(y), colors="b", linestyles="-.",
                       linewidth=3,
                       label="Erste Lockerung(20.04.20)")
        except Exception as e:
            pass
        plt.title('%s(von Sep. 2019 bis Sep. 2020)'%categoryName, fontsize=15)
        plt.xlabel("Datum")
        plt.ylabel("durchschnittliche Produktpreise (€)")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        fig.savefig("image/%s.svg"%categoryName)
        plt.show()

    ###################function for plotting the trend of different Category in one graph#####################################
    def plot_all_categories(dict_top_category):
       databaseProcessor = DatabaseProcessor.DatabaseProcesser()
       databaseProcessor.db = pymysql.connect("localhost", "root", "6857", "IdealoPreis")
       fig = plt.figure(figsize=(12,6))
       for key,value in dict_top_category.items():
          x,y = databaseProcessor.get_average_eachCategory(key)
          plt.plot(x,y,label = value)
       plt.title("Durchschnittliche Preisentwicklung nach Kategorien(von Sep. 2019 bis Sep. 2020)", fontsize=15)
       plt.xlabel("Datum")
       plt.ylabel("durchschnittliche Produktpreise (€)")

       plt.legend()
       plt.grid()
       plt.tight_layout()
       fig.savefig('image/Categories.svg')
       plt.show()