from os import listdir
from os.path import isfile, join
import csv


def collectSleepData(path):

    #path = "C:/Users/nadle/Documents/GarminData/Sleep"
    dataFiles = [f for f in listdir(path) if isfile(join(path, f))]

    sortedFiles = []
    tempArray = []
    dayArray = []
    counter = 0
    extractedData = []

    #Das Array mit den Dokumentnamen nach Datum sortieren
    for x in range(5):          
        for y in range(len(dataFiles)):
            if(int(dataFiles[y][-6:-4]) == x+2):
                tempArray.append(dataFiles[y])
                dayArray.append(dataFiles[y][-9:-7])
        dayArray.sort()
        for i in range(len(dayArray)):
            for u in range(len(tempArray)):
                if(dayArray[i] == tempArray[u][-9:-7]):
                    sortedFiles.append([tempArray[u]])
        dayArray=[]
        tempArray=[]
    # Now the Sleep data files are sorted by date. They are in the list "sortedFiles"

    # Now we extract the data from the files and remove the uncecessary data
    for x in range(len(sortedFiles)):
        pathString = path + '/'.join(sortedFiles[x])
        with open(pathString, newline='') as csvfile:
            fileData = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in fileData:
                if(counter > 0 and counter < 7):
                    if(counter!=1):
                        # Change hour format to minute format. Remove any letters or whitespaces.
                        row[1] = row[1].replace('m','').replace(' ','').replace('-','')
                        if(row[1]):
                            index = row[1].find('h')
                            if(index>=0):
                                row[1] = row[1].replace('h', '')
                                row[1] = int(row[1][0:index])*60 + int(row[1][index:None])
                    for i in range(len(row)):
                        # Fill empty rows with '0' to prevent "undefined errors".
                        if(not row[i]):
                            row[i] = "0"
                    tempArray.append(row[1])
                counter += 1
            counter = 0
            extractedData.append(tempArray)
            tempArray = []
    return extractedData
    # Now we have all data in the "extractedData" List in the following order: Date; Total Sleeptime; Deep; Light; REM; Awake;      All times have been converted to the unit 'MINUTE'
   