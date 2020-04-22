import animation
from os import system, name

from algorithm import algMain

def printTitle():
    print("\t----- Stock Market Prediction and Portfolio Tool -----")

def getStocksFromUser():
    print("Enter The Stocks In Question, Separated By Commas")
    stocks = input(">>> ")
    return stocks

def runAlgorithm(listOfStocks):
    clear()
    print("Running Predictive Pricing of", listOfStocks, "stocks")
    algMain(listOfStocks)

def main():
    clear()
    printTitle()
    stocksText = getStocksFromUser()
    stocks = stocksText.lower().replace(" ", "").split(",")
    runAlgorithm(stocks)
    #print(stocks)
    
def clear():
    system('cls')

main()

