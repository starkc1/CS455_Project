from time import sleep
import numpy as np
import pandas as pd

from sklearn import linear_model


def loadTrainingData():
    train_fd001 = np.genfromtxt("Data/train_FD001.txt")
    train_fd002 = np.genfromtxt("Data/train_FD002.txt")
    train_fd003 = np.genfromtxt("Data/train_FD003.txt")
    train_fd004 = np.genfromtxt("Data/train_FD004.txt")
    
    return train_fd001, train_fd002, train_fd003, train_fd004

def loadTestData():
    test_fd001 = np.genfromtxt("Data/test_FD001.txt")
    test_fd002 = np.genfromtxt("Data/test_FD002.txt")
    test_fd003 = np.genfromtxt("Data/test_FD003.txt")
    test_fd004 = np.genfromtxt("Data/test_FD004.txt")

    return test_fd001, test_fd002, test_fd003, test_fd004

def loadRULData():
    rul_fd001 = np.genfromtxt("Data/RUL_FD001.txt")
    rul_fd002 = np.genfromtxt("Data/RUL_FD002.txt")
    rul_fd003 = np.genfromtxt("Data/RUL_FD003.txt")
    rul_fd004 = np.genfromtxt("Data/RUL_FD004.txt")

    return rul_fd001, rul_fd002, rul_fd003, rul_fd004

def algMain():
    train_fd001, train_fd002, train_fd003, train_fd004 = loadTrainingData()
    test_fd001, test_fd002, test_fd003, test_fd004 = loadTestData()
    rul_fd001, rul_fd002, rul_fd003, rul_fd004 = loadRULData()

    








    return
    