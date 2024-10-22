import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


#df.drop(["Total_Sleep", "Date_Time", "Deep_Sleep", "Light_Sleep", "REM_Time", "Awake", "Intensity", "Steps", "Stress", "Elevation_Up", "Elevation_Down"], axis = 1, inplace=True)
# Download and prepare the data
data_root = "C:/Users/nadle/Documents/GarminData/SleepExport/Schlafdaten.csv"
df = pd.read_csv(data_root)

totalSleepCol = 2
deepSleepCol = 3 
LightSleepCol = 4
RemCol = 5
AwakeCol = 6

df["REM_Time"] = df["REM_Time"].astype(float)
df["Deep_Sleep"] = df["Deep_Sleep"].astype(float)
df["Light_Sleep"] = df["Light_Sleep"].astype(float)
df["Awake"] = df["Awake"].astype(float)

for index in reversed(range(len(df))):
    if(df.iloc[index]["Total_Sleep"] == 0):
        df = df.drop(index)
    else:
        if df.iat[index, deepSleepCol]:
            df.iat[index, deepSleepCol] = round(df.iat[index, deepSleepCol]/df.iat[index, totalSleepCol]*100,2)
        if df.iat[index, LightSleepCol]:
            df.iat[index, LightSleepCol] = round(df.iat[index, LightSleepCol]/df.iat[index, totalSleepCol]*100,2)
        if df.iat[index, AwakeCol]:
            df.iat[index,AwakeCol] = round(df.iat[index, AwakeCol]/df.iat[index, totalSleepCol]*100,2)
        if df.iat[index, RemCol]:
            df.iat[index,RemCol] = round(df.iat[index, RemCol]/df.iat[index, totalSleepCol]*100,2)
            



df.index = pd.to_datetime(df["Date"])

#Plotting the first table
firstTable = [df[["REM_Time", "Deep_Sleep"]], df[["Intensity"]]]

firstTable[0].plot(ylim=(0,100),ylabel="Schlafdaten")
firstTable[1].plot(secondary_y=True, ax=plt.gca(), ylabel="Intensität")

#Plotting the second table
secondTable = [df[["Light_Sleep", "Awake"]], df[["Intensity"]]]

secondTable[0].plot(ylim=(0,100),ylabel="Schlafdaten")
secondTable[1].plot(secondary_y=True, ax=plt.gca(), ylabel="Intensität")

#Plotting the third table
thirdTable = [df[["Total_Sleep"]], df[["Stress"]]]

thirdTable[0].plot(ylabel="Schlafdaten")
thirdTable[1].plot(secondary_y=True, ax=plt.gca(), ylabel="Stress")

#Plotting the fourth table
fourthTable = [df[["Light_Sleep", "Awake"]], df[["Stress"]]]

fourthTable[0].plot(ylim=(0,100),ylabel="Schlafdaten")
fourthTable[1].plot(secondary_y=True, ax=plt.gca(), ylabel="Stress")


plt.show()

