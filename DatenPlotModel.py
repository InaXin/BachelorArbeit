import matplotlib.pyplot as plt
import pandas as pd
import pymysql
import DatabaseProcessor


class DatenPlotModel:

    #===========================Toilettenartikel plotting===============================================================
    def plot_toilettenartikel(x,y):
        fig = plt.figure(figsize=(12, 6))
        plt.plot(x, y, marker = 'x')
        plt.title("Durchschnittliche Preisentwicklung von Kategorie 'Toilettenartikel'", fontsize=16)
        plt.xlabel("Datum")
        plt.ylabel("durchschnittliche Produktpreise (€)")
        plt.grid()
        plt.tight_layout()
        fig.savefig('image/Toilettenartikel_Preisentwicklung.svg')
        plt.show()
    #===========================Desinfektionsmittel plotting============================================================

    def plot_desinfektionsmittel(x, y):
        fig = plt.figure(figsize=(12, 6))
        plt.plot(x, y, marker='x')
        plt.title("Durchschnittliche Preisentwicklung von Kategorie 'Desinfektionsmittel'", fontsize=16)
        plt.xlabel("Datum")
        plt.ylabel("durchschnittliche Produktpreise (€)")
        plt.grid()
        plt.tight_layout()
        fig.savefig('image/Desinfektionsmittel_Preisentwicklung.svg')
        plt.show()

    #===========================Handys plotting=========================================================================

    def plot_handys(x, y):
        fig = plt.figure(figsize=(12, 6))
        plt.plot(x, y, marker='x')
        plt.title("Durchschnittliche Preisentwicklung von Handys", fontsize=16)
        plt.xlabel("Datum")
        plt.ylabel("durchschnittliche Produktpreise (€)")
        plt.grid()
        plt.tight_layout()
        fig.savefig('image/Handys_Preisentwicklung.svg')
        plt.show()










