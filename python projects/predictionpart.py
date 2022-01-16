from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
import csv
import pandas as pd
import basics3
import creatingcsv2
import glob

data = pd.read_csv("data1.csv", index_col=False)
predictors = data.drop(["outcomes"], axis=1)
outcomes = data["outcomes"]
knn = KNeighborsClassifier(n_neighbors = 2)
#standardpredictors = preprocessing.scale(predictors)
knn.fit(predictors, outcomes)




sk_predictions = knn.predict(predictors)
print(accuracy_score(sk_predictions, outcomes))

testdata = []
testnorth = []
testsouth = []
#test = basics3.get_normed_predictors("c:/Users/Mishal/Desktop/testing.png",0)
testpngs = glob.glob("c:/Users/Mishal/Desktop/testpics/*.png")
for png in testpngs:
    testdata.append(basics3.get_normed_predictors(png))
    testnorth.append(basics3.checknorth[png.split("\\")[-1].split("test.png")[0]])
    testsouth.append(basics3.checksouth[png.split("\\")[-1].split("test.png")[0]])
        #print(basics2.get_normed_predictors("c:/Users/Mishal/Desktop/testing.png", rotation))


test2 = basics3.get_normed_predictors("c:/Users/Mishal/Desktop/constellations/ursa_major.png",0)
test2.append(1)
test2.append(0)
test2 = [test2]
#testing = [test]
df2 = pd.DataFrame(test2)
df2 = df2.T
df = pd.DataFrame(testdata)
df["north"] = testnorth
df["south"] = testsouth
df.columns = creatingcsv2.columns
print(accuracy_score(knn.predict(df), range(1,11)))
knn.predict(df)