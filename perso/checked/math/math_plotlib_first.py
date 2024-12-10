import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2,10)
y1=x**2
y2=x**3
print(x)


#plt.figure(figsize=(12,8))
plt.subplot(2,1,1)
plt.plot(x,y1,c='red',label="first graph",lw=2,ls='--')
plt.plot(x,y2,c='purple',label='second')
plt.xlabel('axe x')
plt.ylabel('axe y')
plt.legend()
plt.savefig('fig1.png')
plt.subplot(2,1,2)
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.plot(np.sin(x),np.cos(x))
plt.show()
