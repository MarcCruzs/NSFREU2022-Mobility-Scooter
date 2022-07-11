import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
import copy
from csv import writer
'''pd.read_csv is used to read a csv file that is supposed to have a collection of instances of differing labels/Targets
that will be filtered through'''
Main = pd.read_csv('MobilityScooterData.csv', names = ["Target", "X","Y","Z","GX","GY","GZ"])
print(Main['Target'].value_counts())

Normal = copy.deepcopy(Main)
#Sudden Acceleration (SA)
#Sudden Left Turn (SLT)
#Sudden Right Turn (SRT)
#Sudden Break (SB)
SA = copy.deepcopy(Main)
SLT = copy.deepcopy(Main)
SRT = copy.deepcopy(Main)
SB = copy.deepcopy(Main)
#Sudden Acceleration (1), Sudden Right Turn (2), Sudden Left Turn (3), Sudden Break (4), and Normal (5)
'''How the filter function works is it starts with what you want to name the csv file. Then whichever corresponding
array that is supposed to go with that csv file. Then value1-value4 are the values you want to get rid of. 
NOTE: used pandas drop function to remove each row with a specific value for the column "Target."'''
def Filter(name, lst, value1,value2,value3,value4):
    lst.drop(lst[lst['Target'] == value1].index, inplace = True)
    lst.drop(lst[lst['Target'] == value2].index, inplace = True)
    lst.drop(lst[lst['Target'] == value3].index, inplace = True)
    lst.drop(lst[lst['Target'] == value4].index, inplace = True)
    lst.to_csv('Filtered/{0}.csv'.format((name)))

Filter('Normal',Normal, 1,2,3,4) #5
Filter('Sudden Acceleration',SA, 2,3,4,5) #1
Filter('Sudden left Turn',SLT,1,2,4,5) #3
Filter('Sudden Break',SB,1,2,3,5) #4
Filter('Sudden Right Turn',SRT,1,3,4,5) #2

