import animation
from os import system, name

from algorithm import algMain

def printTitle():
    print("\t----- Stock Market Prediction Tool -----")

def getStocksFromUser():
    print("Enter The Stocks In Question, Separated By Commas")
    stocks = input(">>> ")
    return stocks

def getForcastFromUser():
    print("Enter How Many Days To Forecast Stock Prices")
    forecast = input(">>> ")
    return forecast

@animation.wait('spinner')
def runAlgorithm(listOfStocks, forecast):
    clear()
    print("Running Predictive Pricing of", listOfStocks, "Stocks At A", forecast, "Day Forecast")
    loading = animation.Wait()
    loading.start()
    algMain(listOfStocks, forecast)
    loading.stop()

def main():
    clear()
    printTitle()
    stocksText = getStocksFromUser()
    stocks = stocksText.lower().replace(" ", "").split(",")
    forecast = getForcastFromUser()
    runAlgorithm(stocks, forecast)
    #print(stocks)
    
def clear():
    system('cls')

main()

