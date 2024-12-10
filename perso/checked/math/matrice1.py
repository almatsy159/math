M33=[[0,0,1],[0,1,0],[1,0,1]]


def create_matrice(x):
    matrice=[]
    i=0
    while i < x:
        osef = "x"+str(i)
        osef = []
        matrice.append(osef)
        i += 1
    return matrice

long=4
y1=create_matrice(long)
y2=create_matrice(long)
#print(y)
suite=[0,1,2,3]
suite2=[3,2,1,0]

def fill_matrice(suite,matrice,rang):
    for i in range(len(matrice)):
        matrice[i]=create_matrice(rang+1)
        #print(suite[i])
        #print(matrice[i])
        matrice[i][rang]=suite[i]
        print("suite :",suite,"; matrice :",matrice,"; rang :",rang)
    return matrice

# lambda = create_matrice => associe la fonction !!!
#print(y1)
z1=fill_matrice(suite,y1,0)
z2=fill_matrice(suite2,y2,0)
#print(y2)
print(z1)
print(z2)

"""
long=len(suite)
compt=0
for i in M33 :
    osef= create_matrice(long-1)
    for j in range(len(osef)):
        #osef[compt].append([])
        #print("osef :",osef)
        osef = fill_matrice(i,osef,compt)
    #print("temp :",temp)
    #osef.append(temp)
    compt +=1
print(osef)
"""


def rowToCol(matrice):
    x=len(matrice)
    k=[]
    while len(k) < x:
        k.append([])
        print(k)
        compt=0
        for i in matrice :
            #i=row
            temp = create_matrice(x)
            for j in range(len(i)):
                temp[j]=i[j]
            compt +=1
