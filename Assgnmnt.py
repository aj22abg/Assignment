# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 20:22:20 2022

@author: LENOVO
"""

import pandas as pd
import matplotlib.pyplot as plt
#reading the csv file
read_data = pd.read_csv("Assignment.csv")
print(read_data)
plt.figure()
#function to plot the linegraph
def graph():
    plt.plot(read_data["Country Name"],read_data["1990"],label=1990)
    plt.plot(read_data["Country Name"],read_data["2000"],label=2000)
    plt.plot(read_data["Country Name"],read_data["2019"],label=2019)
    plt.xlabel("Country")
    plt.ylabel("CO2 emission(kt)")
    plt.xticks(rotation=90)
    plt.title("Co2 Emission")
    plt.legend()
    #saving the figure
    plt.savefig("Linegraph.png", bbox_inches="tight")
    plt.show()
    
#Calling the function to plot linegraph    
graph()


#function to plot the bargraph
def barfn():
    plt.bar(read_data["Country Name"],read_data["2019"],alpha=0.4, color="Blue")
    plt.xlabel("Country")
    plt.ylabel("CO2 emission(kt)")
    plt.xticks(rotation=90)
    plt.title("Co2 Emission")
    plt.legend()
    #saving the bargraph
    plt.savefig("Bargraph.png", bbox_inches="tight")
    plt.show()
#calling the function to plot the bargraph
barfn()


#Function to plot Piechart
def piechrt():
    plt.pie(read_data["2019"],autopct='%1.1f%%',startangle=90)
    plt.title("CO2 emission(kt)")
    plt.legend(bbox_to_anchor = (1,1),labels=read_data["Country Name"])
    #saving the Piechart
    plt.savefig("Piechart.png", bbox_inches="tight")
    plt.show()

#calling the function to plot the piechart
piechrt()