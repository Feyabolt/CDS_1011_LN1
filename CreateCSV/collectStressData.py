from os import listdir
from os.path import isfile, join
import csv



def collectStressData(path):

    #path = "C:/Users/nadle/Documents/GarminData/Sleep"
    dataFiles = [f for f in listdir(path) if isfile(join(path, f))]

    monthConv = [["Jan", '01'],["Feb", '02'],["Mrz", '03'],["Apr", '04'],["Mai", '05'],["Jun", '06']]
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
                   for y in range(len(monthConv)):
                       if(monthConv[y][0] == row[0][0:3]):
                           if(len(row[0]) == 5):
                               row[0] = row[0][0:4] + '0' + row[0][-1:None]
                           row[0] = "2023-" + monthConv[y][1] + '-' + row[0][-2:None]
                   extractedData.append(row)
                counter += 1
            counter = 0
    return extractedData
    # Now we have all data in the "extractedData" List in the following order: Date; Total Sleeptime; Deep; Light; REM; Awake;      All times have been converted to the unit 'MINUTE'
