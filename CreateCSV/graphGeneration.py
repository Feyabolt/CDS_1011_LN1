import matplotlib.pyplot as plt
import pandas as pd


# Import and prepare the data
data_root = "GarminData/DataExport/Schlafdaten.csv"
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
    # Dropping every col that has no recorded sleep data
    if(df.iloc[index]["Total_Sleep"] == 0):
        df = df.drop(index)
    # Rounding the different sleep Data based on total amount of sleep
    else:
        if df.iat[index, deepSleepCol]:
            df.iat[index, deepSleepCol] = round(df.iat[index, deepSleepCol]/df.iat[index, totalSleepCol]*100,2)
        if df.iat[index, LightSleepCol]:
            df.iat[index, LightSleepCol] = round(df.iat[index, LightSleepCol]/df.iat[index, totalSleepCol]*100,2)
        if df.iat[index, AwakeCol]:
            df.iat[index,AwakeCol] = round(df.iat[index, AwakeCol]/df.iat[index, totalSleepCol]*100,2)
        if df.iat[index, RemCol]:
            df.iat[index,RemCol] = round(df.iat[index, RemCol]/df.iat[index, totalSleepCol]*100,2)
            

indexStartTime = pd.Timestamp('2023-02-19')
indexEndTime = pd.Timestamp('2023-06-07')

df.index = pd.to_datetime(df["Date"])

# Plotting the first table
firstTable = [df[["Total_Sleep"]], df[["Stress"]]]

firstTable[0].plot(ylim=(150,700),ylabel="Sleep Time (min)",xlim=(indexStartTime,indexEndTime)).grid(axis='y')
firstTable[1].plot(secondary_y=True, ax=plt.gca(), ylabel="Stress")

# Plotting the second table
secondTable = [df[["Light_Sleep"]], df[["Stress"]]]

secondTable[0].plot(ylim=(0,100),ylabel="Light sleep (%)",xlim=(indexStartTime,indexEndTime)).grid(axis='y')
secondTable[1].plot(secondary_y=True, ax=plt.gca(), ylabel="Stress")

# Plotting the third table
thirdTable = [df[["Deep_Sleep"]], df[["Stress"]]]

thirdTable[0].plot(ylabel="Deep Sleep (%)",xlim=(indexStartTime,indexEndTime)).grid(axis='y')
thirdTable[1].plot(secondary_y=True, ax=plt.gca(), ylabel="Stress")

# Plotting the fourth table
fourthTable = [df[["Light_Sleep"]], df[["Intensity"]]]

fourthTable[0].plot(ylim=(0,100),ylabel="Light Sleep (%)",xlim=(indexStartTime,indexEndTime)).grid(axis='y')
fourthTable[1].plot(secondary_y=True, ax=plt.gca(), ylabel="Intensity")

# Plotting the fifth table
fifthTable = [df[["Deep_Sleep"]], df[["Intensity"]]]

fifthTable[0].plot(ylim=(0,100),ylabel="Deep Sleep (%)",xlim=(indexStartTime,indexEndTime)).grid(axis='y')
fifthTable[1].plot(secondary_y=True, ax=plt.gca(), ylabel="Intensity")

plt.show()

