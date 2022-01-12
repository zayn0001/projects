import numpy as np
import scipy.stats as ss
import pandas as pd



#csv_data = csv.reader(data)
#csv_lines = list(csv_data)
#total columns = 15 including srl.no and quality boolean
#total criteria = 13 from 1 - 14
#table = np.array(csv_lines[1::])

#points = table[:300,1:3]
#booleans = table[:300,14]


#predictors = np.zeros((len(points), len(points[0])))
#for ind in range(predictors.shape[0]):
#    for i in range(predictors.shape[1]):
#        predictors[ind][i] = float(points[ind][i])

#outcomes = np.zeros(len(booleans))
#for ind in range(len(booleans)):
#    outcomes[ind] = int(booleans[ind])
  
data = pd.read_csv('C:\\Users\\mishal\\Desktop\\wine.csv', encoding='utf-8')
data = pd.DataFrame(data)
colors = data['color']
is_red = [(color=='red')*1 for color in colors]
data['color'] = is_red
print(data)
#predictors = np.transpose(np.array([data['sulphates'], data['alcohol']]))[:100]
outcomes = np.array(data['high_quality'])
predictors = data.drop(['high_quality'], axis=1)
print(predictors)

from sklearn import preprocessing
standard_predictors = preprocessing.scale(predictors)
print(standard_predictors)

def find_mode(total):
    (mode_list, count) = ss.mstats.mode(total)
    return mode_list[0]
            

def dist(p1,p2):
    return np.sqrt(np.sum(np.power(p2-p1,2)))
    
def knn_predict(p, predictors, outcomes, k=5):
    distances = np.zeros(predictors.shape[0])
    for i in range(len(distances)):
        distances[i] = dist(p , predictors[i])
        ind = distances.argsort()
    return find_mode(outcomes[ind[:k]])

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(standard_predictors, outcomes)
'''
def make_pg(predictors, outcomes, limits, h, k):
    
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs,ys)
    
    prediction_grid = np.zeros(xx.shape, dtype=int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x,y])
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)
    return (xx,yy,prediction_grid)
'''
#high = predictors[outcomes=='1']
#low = predictors[outcomes=='0']
#plt.plot(low[:,0],low[:,1], 'ro', markersize = 2)
#plt.plot(high[:,0],high[:,1], 'bo', markersize = 2)
#plt.show()
'''   
def plot_prediction_grid (xx, yy, prediction_grid):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
'''  
'''
k=5
limits = (0, 1, 8, 15)
h=0.05
(xx,yy,prediction_grid) =  make_pg(predictors, outcomes, limits, h, k)  
plot_prediction_grid(xx, yy, prediction_grid)
'''
#total = 600
#standard_predictors = standard_predictors[:total]
#outcomes = outcomes[:total]

sk_predictions = knn.predict(standard_predictors)
#my_predictions = np.array([knn_predict(p, standard_predictors, outcomes) for p in standard_predictors])

#print(100*np.mean(my_predictions==outcomes))
print(100*np.mean(sk_predictions==outcomes))