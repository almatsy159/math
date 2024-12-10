import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2,10)
y=x**2
y2=x**3
print(x)

#dataset={f"experience{i}":np.random.randn(100) for i in range(4)}

"""
def graphique(dataset):
"""
fig, axe= plt.subplots(2,1,sharex=True)
#type ax
axe[0].plot(x,y)
axe[1].plot(x,np.sin(x))
plt.show()
