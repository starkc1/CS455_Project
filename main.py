import animation
import time
from time import sleep
from os import system, name 
from enum import Enum



from algorithm import longFunctionTest


def printTitle():
    print("\t------ Engine Degredation Prediction Tool ------")

def getLevel():
    print("\nInsert The Level Of Predictive Warning Desired From The Following:")
    print("\n1. Initial Degredation")
    print("2. Mid Degredation")
    print("3. Pre Fault")
    print("4. At Fault")
    return input("Insert 1-4: >>> ")

def convertLevelToText(level):
    if (level == "1"):
        return "Initial Degredation"
    elif (level == "2"):
        return "Mid Degredation"
    elif (level == "3"):
        return "Pre Fault"
    elif (level == "4"):
        return "At Fault"

@animation.wait('spinner')
def runAlgorithm(level):
    clear()
    levelText = convertLevelToText(level)
    print("Running Predictive Tooling at", levelText, "Level")
    loading = animation.Wait()
    loading.start()
    longFunctionTest()
    loading.stop()

def clear():
    system('cls')

def main():
    clear()
    printTitle()
    predictiveLevel = getLevel()
    runAlgorithm(predictiveLevel)


main()