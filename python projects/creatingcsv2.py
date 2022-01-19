import csv
import pandas as pd
import glob   
import basics3
import math

const_pngs = glob.glob("c:/Users/Mishal/Desktop/constellations/*.png")




predictors = []
outcomes = []
north = []
south = []
i = 1
for png in const_pngs:
    #for rotation in range(0, 460, 20):    
    predictors.append(basics3.get_normed_predictors(png))
    outcomes.append(i)
    north.append(basics3.checknorth[png.split("\\")[-1].split(".png")[0]])
    south.append(basics3.checksouth[png.split("\\")[-1].split(".png")[0]])
    i = i+1



noofpredictors = math.factorial(basics3.NO_OF_POINTS)/(math.factorial(basics3.NO_OF_POINTS-2)*2)
noofpredictors = int(noofpredictors)
with open("mlforconsts.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["predictor"]*noofpredictors)
    csvwriter.writerows(predictors)

data = pd.read_csv("mlforconsts.csv")
data["north"] = north
data["south"] = south
data["outcomes"] = outcomes


data.to_csv('data1.csv', index=False)

columns = data.drop(["outcomes"], axis=1).columns
#data["outcomes"] = [1]*len()
