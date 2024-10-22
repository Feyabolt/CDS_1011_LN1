import csv
from collectSleepData import collectSleepData
from collectIntensityData import collectIntensityData
from collectStressData import collectStressData
from collectStepData import collectStepData
from collectElevationData import collectElevationData
from datetime import datetime

stepDataPath = "C:/Users/nadle/Documents/GarminData/Steps/"
sleepDataPath= "C:/Users/nadle/Documents/GarminData/Sleep/"
intensityDataPath = "C:/Users/nadle/Documents/GarminData/Intensity/"
stressDataPath = "C:/Users/nadle/Documents/GarminData/Stress/"
elevationDataPath = "C:/Users/nadle/Documents/GarminData/Elevation/"

sleepData = collectSleepData(sleepDataPath)
intensityData = collectIntensityData(intensityDataPath)
stressData = collectStressData(stressDataPath)
stepData = collectStepData(stepDataPath)
elevationData = collectElevationData(elevationDataPath)
outputList = []

def generateCSV():
    for x in range(len(sleepData)):
        for y in range(len(intensityData)):
            if(intensityData[y][0] == sleepData[x][0]):
                sleepData[x].append(intensityData[y][1])

        for y in range(len(stepData)):
            if(stepData[y][0] == sleepData[x][0]):
                sleepData[x].append(stepData[y][1])

        for y in range(len(stressData)):
            if(stressData[y][0] == sleepData[x][0]):
                sleepData[x].append(stressData[y][1])

        for y in range(len(elevationData)):
            if(elevationData[y][0] == sleepData[x][0]):
                sleepData[x].append(elevationData[y][1])
                sleepData[x].append(elevationData[y][2])
        sleepData[x].insert(1,datetime.timestamp(datetime.strptime(sleepData[x][0],'%Y-%m-%d')))
        

    outputList = sleepData
    with open('C:/Users/nadle/Documents/GarminData/SleepExport/Test.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["Date", "Date_Time", "Total_Sleep", "Deep_Sleep", "Light_Sleep", "REM_Time", "Awake", "Intensity", "Steps", "Stress", "Elevation_Up", "Elevation_Down"])
        for x in range(len(outputList)):
            writer.writerow(outputList[x])



userInput = input("Geben Sie Ihren gewünschten Vorgang an:\n\t1: Neues CSV mit den Gesundheitsdaten erstellen\n\nIhre Auswahl: ")
match userInput:
    case "1":
        generateCSV()