import matplotlib.pyplot as plt
import pandas as pd
import pymysql
import DatabaseProcessor


class DatenPlotModel:

    def plot_category(x, y,CategoryName:str):
        fig = plt.figure(figsize=(12, 6))
        plt.plot(x, y, marker='x')
        plt.title("Durchschnittliche Preisentwicklung von Kategorie '%s'" % CategoryName, fontsize=16)
        plt.xlabel("Datum")
        plt.ylabel("durchschnittliche Produktpreise (€)")
        plt.grid()
        plt.tight_layout()
        #fig.savefig('image/%s_Preisentwicklung.svg' % CategoryName)
        plt.show()












