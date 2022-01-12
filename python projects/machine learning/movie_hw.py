import numpy as np
import pandas as pd

from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score

import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt

database = pd.read_csv('C:\\Users\\mishal\\Desktop\\movie_db_hw.csv')
#removing ones with missing values
database = database.dropna()
database = database.reset_index(drop=True)

#extracting all unique genres
genres = []
for a in database.genres:
    genres.extend(str(a).split(', '))
unique_genres = list(set(genres))

#creating a dataframe with only important columns
movie_df = pd.DataFrame([database['budget'],database['vote_count'], database['vote_average'], database['popularity'], database['runtime'], database['revenue']]).T
movie_df['profitable'] = (database['revenue']>database['budget']).astype(int)

#creating column for every genre
for genre in unique_genres:
    movie_df[genre] = [int(str(genre) in str(database['genres'][i])) for i in range(len(database))]


regression_target = 'revenue'
classification_target = 'profitable'
continuous_covariates = ['budget', 'popularity', 'runtime', 'vote_count', 'vote_average']
outcomes_and_continuous_covariates = continuous_covariates + [regression_target, classification_target]
all_covariates = continuous_covariates + unique_genres

#specifying different important dataframes
regression_outcome = movie_df[regression_target]
classification_outcome = movie_df[classification_target]
covariates = movie_df[all_covariates]

#plotting_variables = ['budget', 'popularity', regression_target]
#axes = pd.plotting.scatter_matrix(database[plotting_variables], alpha=0.15, \
#       color=(0,0,0), hist_kwds={"color":(0,0,0)}, facecolor=(1,0,0))
#plt.show()

#fix right skewing
skews = []
old_skews = []
for col in outcomes_and_continuous_covariates:
    old_skews.append(movie_df[col].skew())
    if movie_df[col].skew() > 0:
        movie_df[col] = np.log10(movie_df[col].astype(float) + np.repeat(1, len(movie_df)))
    skews.append(movie_df[col].skew())

movie_df.to_csv('C:\\Users\\mishal\\Desktop\\movie_clean.csv')

linear_regression = LinearRegression()
logistic_regression = LogisticRegression()
forest_regression = RandomForestRegressor(max_depth=4, random_state=0)
forest_classifier = RandomForestClassifier(max_depth=4, random_state=0)

def correlation(estimator, X, y):
    estimator.fit(X, y)
    prediction = estimator.predict(X)
    return r2_score(prediction,y)

def accuracy(estimator, X, y):
    estimator.fit(X, y)
    prediction = estimator.predict(X)
    return accuracy_score(prediction,y)

    
logistic_regression_scores = cross_val_score(logistic_regression, covariates, classification_outcome,cv=10, scoring=accuracy)  
forest_classification_scores = cross_val_score(forest_classifier, covariates, classification_outcome,cv=10, scoring=accuracy)
linear_regression_scores = cross_val_score(linear_regression, covariates, regression_outcome,cv=10, scoring=correlation)  
forest_regression_scores = cross_val_score(forest_regression, covariates, regression_outcome,cv=10, scoring=correlation)

plt.figure()
plt.axes().set_aspect('equal', 'box')
plt.scatter(logistic_regression_scores, forest_classification_scores)
#plt.plot((0, 1), (0, 1), 'k-')

#plt.xlim(0, 1)
#plt.ylim(0, 1)
plt.xlabel("Linear Classification Score")
plt.ylabel("Forest Classification Score")







positive_revenue_df = movie_df[movie_df['revenue']>0]

# Replace the dataframe in the following code, and run.
regression_outcome = positive_revenue_df[regression_target]
classification_outcome = positive_revenue_df[classification_target]
covariates = positive_revenue_df[all_covariates]

# Reinstantiate all regression models and classifiers.
linear_regression = LinearRegression()
logistic_regression = LogisticRegression()
forest_regression = RandomForestRegressor(max_depth=4, random_state=0)
forest_classifier = RandomForestClassifier(max_depth=4, random_state=0)
linear_regression_scores = cross_val_score(linear_regression, covariates, regression_outcome, cv=10, scoring=correlation)
forest_regression_scores = cross_val_score(forest_regression, covariates, regression_outcome, cv=10, scoring=correlation)
logistic_regression_scores = cross_val_score(logistic_regression, covariates, classification_outcome, cv=10, scoring=accuracy)
forest_classification_scores = cross_val_score(forest_classifier, covariates, classification_outcome, cv=10, scoring=accuracy)

plt.figure()
plt.axes().set_aspect('equal', 'box')
plt.scatter(logistic_regression_scores, forest_classification_scores)
plt.plot((0, 1), (0, 1), 'k-')

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("Linear Classification Score")
plt.ylabel("Forest Classification Score")
    
# Print the importance of each covariate in the random forest classification.
forest_classifier.fit(covariates, classification_outcome)
#sorted(list(zip(all_covariates, forest_classifier.feature_importances_)), key=lambda tup: tup[1])

    
    
   
    

