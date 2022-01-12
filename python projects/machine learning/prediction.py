import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
from collections import Counter
import random
from sklearn import datasets


def dist(p1,p2):
	return np.sqrt(np.sum(np.power(p2-p1,2)))

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
    
    
def make_pg(predictors, outcomes, limits, h, k):
    '''
    prediction grid
    '''
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

def find_nn(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = dist(p , points[i])
        ind = distances.argsort()
    distances = distances[ind]
    return ind[:k]

def find_mode(votes):
    winners = []
    freq_list = Counter(votes)
    largest_freq = max(freq_list.values())
    for vote, freq in freq_list.items():
        if freq == largest_freq:
            winners.append(vote)
    return random.choice(winners)
def knn_predict(p, points, categories, k=5):
    ind = find_nn(p, points, k)
    return find_mode(categories[ind])

def create_sd(n=50):
    '''
    Syntheti Data
    Create two sets of points from bivariate normal distribution
    '''
    points = np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,1).rvs((n,2))), axis=0)
    outcomes = np.concatenate((np.repeat(0,n), np.repeat(1,n)))
    return (points, outcomes)

iris = datasets.load_iris()
predictors = iris.data[:,0:2]
outcomes = iris.target
plt.plot(predictors[outcomes==0][:,0], predictors[outcomes==0][:,1], 'ro')
plt.plot(predictors[outcomes==1][:,0], predictors[outcomes==1][:,1], 'go')
plt.plot(predictors[outcomes==2][:,0], predictors[outcomes==2][:,1], 'bo')

k = 5
limits = (4, 8, 1.5, 4.5)
h=0.1
(xx, yy, prediction_grid ) = make_pg(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid)



from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)
my_predictions = np.array([knn_predict(p, predictors, outcomes, k) for p in predictors])
print(100*np.mean(sk_predictions==my_predictions))
print(100*np.mean(sk_predictions==outcomes))
print(100*np.mean(my_predictions==outcomes))
'''
we are predicting the outcome of the predictors
we know what the outcome should be
so we check how accurate our function is
'''































