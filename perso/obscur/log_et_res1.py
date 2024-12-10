import matplotlib.pyplot as plt
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
def deuxN_plusUn(x):
    return (2*x)+1

def nFoisN_plus1(x):
    return x*(x+1)

def sqrt(x):
    return x**(1/2)

def aSurB(x,y):
    return x/y

k=input("nombre d'element")
k=int(k)
for i in range(k):
    l=i*(10**(-1))
    A.append(l)
    B.append(deuxN_plusUn(l))
    C.append(nFoisN_plus1(l))
    D.append(sqrt(B[i]))
    E.append(aSurB(B[i],D[i]))
    F.append(1)


plt.plot(A,B,c='red',label='B(x)=2n+1')
plt.plot(A,C,c='brown',label='C(x)=x(*x+1)')
plt.plot(A,D,c='blue',label='D(x)=sqrt(C(x))')
#plt.plot(A,E,c='purple',label='E(x)=B(x)/D(x)')
plt.plot(A,F,c='black',label='y=1')
plt.legend()
plt.show()
