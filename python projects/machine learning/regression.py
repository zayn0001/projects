import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt


n =100
beta_0 = 5
beta_1 = 2
np.random.seed(1)
x = 10 * ss.uniform.rvs(size=n)
y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0,scale=1,size=n)

plt.figure()
plt.plot(x,y,'o',ms=5)
xx = np.array([0,10])
plt.plot(xx, beta_0+beta_1*xx)
plt.xlabel('x')
plt.ylabel('y')

# residual -- the diff between estimated value of y and true value
#residual squared sum 
def compute_rss(y_estimate, y):
  return sum(np.power(y-y_estimate, 2))
def estimate_y(x, b_0, b_1):
  return b_0 + b_1 * x

rss = compute_rss(estimate_y(x, beta_0, beta_1), y)


rss = []
slopes = np.arange(-10,15,0.001)
for slope in slopes:
    rss.append(np.sum((y- beta_0 - slope * x)**2))

ind_min = np.argmin(rss)
estimated_slope = slopes[ind_min]

plt.figure()
plt.plot(slopes,rss)
plt.xlabel('slopes')
plt.ylabel('rss')


import statsmodels.api as sm
X = sm.add_constant(x)
mod = sm.OLS(y, X)
est = mod.fit()
print(est.summary())

#95% confidence interval = coeff +  coeff * std err 

#tss = variance of true y (y - y_mean)
#R_square = (tss - rss)/rss         rss<<tss means good fit

#multiple linear  regreassion model
 
n = 500
beta_0 = 5
beta_1 = 2
beta_2 = -1
np.random.seed(1)
x_1 = 10*ss.uniform.rvs(size=n)
x_2 = 10*ss.uniform.rvs(size=n)
y = beta_0 + beta_1*x_1+ beta_2*x_2 + ss.norm.rvs(loc=0,scale=1,size=n)

X = np.stack([x_1,x_2],axis=1)

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], y, c=y)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$y$')


from sklearn.linear_model import LinearRegression
lm = LinearRegression(fit_intercept=True)
lm.fit(X,y)

lm.intercept_
lm.coef_[0]
lm.coef_[1]

X_0 = np.array([2,4])
lm.predict(X_0.reshape(1,-1))

lm.score(X,y) # check if estimated y from X is similar to true values y


from sklearn.model_selection import train_test_split
X_train, X_test,y_train,y_test = train_test_split(X, y,train_size=0.5,random_state=1)
lm = LinearRegression(fit_intercept=True)
lm.fit(X_train,y_train)

lm.score(X_test,y_test)

#MSE(mean squared error) =  variance of y with est_y/train_y
#Train/test error rate = prportion of errors 