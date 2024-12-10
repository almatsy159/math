#matplotlib Machine Learnia chaine youtube (15/30)

import numpy as np
import matplotlib.pyplot as plt


from sklearn.datasets import load_iris #1
from mpl_toolkit.mplot3d import Axes3D

# %matplotlib
# plt scatter (1)
iris = load_iris()

x=iris.data
y=iris.data
names=list(iris.target_names)

print(f'x contient {x.shape[0]} examples et {x.shape[1]} variables')
print(f'il y a {np.unique(y)}.size classes')

plt.scatter(x[:,0],x[,:1],c=y,alpha=0.5,s=x[:,2])
plt.xlabel('longueur sepal')
plt.ylabel('largeur sepal')


# graphh 3D

axe = plt.axes(projection='3d')
axe.scatter(x[:,0],x[:,1],x[:,2],c=y)

f= lambda x,y: np.sin(x) + np.cos(x+y)

X=np.linspace(0,5,100)
Y=np.linspace(0,5,100)
X, Y=nb.meshgrid(X, Y)
Z = f(X,Y) #Z.shape

axe2.plot_surface(X,Y,Z) # couleur: cmap=plasma
