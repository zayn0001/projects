import pandas as pd
x = pd.Series([6, 3, 6, 8])
y = pd.Series([6, 3, 6, 8], index = ['q','w','e','r'])
y['w']
y[['w','r']]

age = {'tim':29, 'jim':39, 'kim':25}
z = pd.Series(age)

data = {'name':['tim', 'jim', 'kim', 'sam'],
        'age':[1, 2, 3, 4],
        'zip':[435,4353,4353,5435]}
p = pd.DataFrame(data, columns=['name','age','zip'])

p['name']
p.name

y = pd.Series([6, 3, 6, 8], index = ['q','w','e','r'])
y.index
y.reindex(sorted(y.index))

x = pd.Series([6, 3, 6, 8], index = ['q','w','e','r'])
y = pd.Series([3, 7, 1, 8], index = ['e','q','w','t'])
z = x + y

import numpy as np

whisky = pd.read_csv('C:\\Users\\mishal\\Desktop\\pdfs\\whiskies.txt')
whisky['Region'] = pd.read_csv('C:\\Users\\mishal\\Desktop\\pdfs\\regions.txt')
whisky.iloc[0:10]
whisky.iloc[5:10,0:5]
whisky.columns
flavors = whisky.iloc[:,2:14]

#pearson correlation
corr_flavors = pd.DataFrame.corr(flavors)
#print(corr_flavors)

import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.show()

corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.colorbar()
plt.show()

#spectral co-clustering

from sklearn.cluster.bicluster import SpectralCoclustering

model = SpectralCoclustering(n_clusters = 6, random_state= 0)
model.fit(corr_whisky)

model.row_labels_
np.sum(model.rows_, axis=0)
np.sum(model.rows_, axis=1)
model.rows_

whisky['Group'] = pd.Series(model.row_labels_, index = whisky.index)
whisky = whisky.iloc[np.argsort(model.row_labels_)]
#shows indexes in the order of the argument
print(whisky['Group'])  
whisky = whisky.reset_index(drop=True)
print(whisky['Group'])  
correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlations = np.array(correlations)

plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title('Title')
#plt.colorbar()
#plt.show()

plt.subplot(122)
plt.pcolor(correlations)
#plt.colorbar()
plt.show()






















