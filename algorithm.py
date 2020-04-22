from time import sleep
import numpy as np
import pandas as pd

from sklearn import linear_model


def performRegression(data):
    
    #Sorting the data into proper date and time
    data['Date'] = pd.to_datetime(data.Date, format ='%Y-%m-%d')
    data.index = data['Date']
    #displaying it in descending order
    data = data.sort_index(ascending = True, axis=0)
    #seperate dataset so that new features wont affect data
    new_data = pd.DataFrame(index=range(0,len(data)),columns=['Date','Close'])
    
    for i in range(0,len(data)):
        new_data['Date'][i] = data['Date'][i]
        new_data['Close'][i] = data['Close'][i]

    for i in range(0, len(new_data)):
        if (new_data['Date'][i].weekday() == 0 or new_data['Date'][i].weekday()):
            new_data['mon_fri'][i] = 1
        else:
            new_data['mon_fri'][i] = 0
    

def loadData(stock):
    file = "Stocks/" + stock + ".us.txt"
    i = 0
    headers = []
    data = []
    with open(file, "r") as stockFile:
        for line in stockFile:
            if (i == 0):
                headers = line.strip().replace(" ", "").split(",")
                i += 1
            else:
                data.append(line.strip().replace(" ", "").split(","))

    dataframe = pd.DataFrame(data = data, columns=headers)
    return dataframe

def algMain(listOfStocks):

    #performs regression for each stock individually
    for stock in listOfStocks:
        dataframe = loadData(stock)
        print(dataframe)
        #performRegression(dataframe)
        dateTesting(dataframe)


def dateTesting(data):
    #Sorting the data into proper date and time
    data['Date'] = pd.to_datetime(data.Date, format ='%Y-%m-%d')
    data.index = data['Date']
    #displaying it in descending order
    data = data.sort_index(ascending = True, axis=0)

    date = data['Date'][0]
    print(date.weekday())
    
