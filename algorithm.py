from time import sleep
import numpy as np
import random
import pandas as pd

import plotly.graph_objects as go
import plotly.express as px

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def performRegression(data, stock, forecast):
    
    #Sorting the data into proper date and time
    data['Date'] = pd.to_datetime(data.Date, format ='%Y-%m-%d')
    data.index = data['Date']
    #displaying it in descending order
    data = data.sort_index(ascending = True, axis=0)

    data = data[['Close']]

    forecast_out = forecast
    data['Prediction'] = data[['Close']].shift(-forecast_out)

    X = np.array(data.drop(['Prediction'], 1))
    X = X[:-forecast_out]


    y = np.array(data['Prediction'])
    y = y[:-forecast_out]


    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    model = LinearRegression()

    model.fit(x_train, y_train)

    forecast_prices = np.array(data.drop(['Prediction'], 1))[-forecast_out:]
    predictions = model.predict(forecast_prices)

    
    j = forecast_out
    j_alt = forecast_out - 1
    dataLength = len(data) - 1


    for i in range(j):
        data['Prediction'][dataLength - i] = predictions[j_alt - i]

    xAxis = data.index.values
    closeData = {'Date' : xAxis[:-forecast_out], 'Close' : y} 
    closeValues = pd.DataFrame(data = closeData)
    predictedData = {'Date' : xAxis[len(xAxis)-forecast_out:len(xAxis)], 'Predicted' : predictions}
    predictedValues = pd.DataFrame(data = predictedData)

    fig = px.line(closeValues, x='Date', y='Close')
    fig.add_trace(go.Scatter(x=predictedValues['Date'], y=predictedValues['Predicted'], name="Predicted Values"))
    title = str(forecast) + " Day Forecast For " + stock  
    fig.update_layout(title=title, xaxis_title = "Dates", yaxis_title = "Cost Per Share ($)")
    fig.show()
    return

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

    split = np.array_split(dataframe, 2)

    return pd.DataFrame(data = split[1])

def algMain(listOfStocks, forecast):

    #performs regression for each stock individually
    for stock in listOfStocks:
        dataframe = loadData(stock)
        #print(dataframe)
        performRegression(dataframe, stock.upper(), int(forecast))
    return
        


    
