from os import listdir
from os.path import isfile, join
import csv



def collectStepData(path):

    #path = "C:/Users/nadle/Documents/GarminData/Sleep"
    dataFiles = [f for f in listdir(path) if isfile(join(path, f))]

    sortedFiles = []
    tempArray = []
    dayArray = []
    counter = 0
    extractedData = []

    #Das Array mit den Dokumentnamen nach Datum sortieren
    for y in range(len(dataFiles)):
        dayArray.append(dataFiles[y][-6:-4])
        dayArray.sort()
    for i in range(len(dayArray)):
        for u in range(len(dataFiles)):
            if(dayArray[i] == dataFiles[u][-6:-4]):
                sortedFiles.append([dataFiles[u]])
    # Now the data files are sorted by date. They are in the list "sortedFiles"

    for x in range(len(sortedFiles)):
        pathString = path + '/'.join(sortedFiles[x])
        with open(pathString, newline='') as csvfile:
            fileData = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in fileData:
                if(counter > 0 and row):
                    tempList = row[0].split("/")
                    row[0] = tempList[2] + '-' + tempList[0] + '-' + tempList[1]
                    row.pop()
                    extractedData.append(row)
                counter += 1
            counter = 0
    return extractedData
    # Now we have all data in the "extractedData" List in the following order: Date; Total Sleeptime; Deep; Light; REM; Awake;      All times have been converted to the unit 'MINUTE'
