rot0=[0,1,2,3,4,5,6,7,8]
rot1=[6,3,0,7,4,1,8,5,2]
rot2=[8,7,6,5,4,3,2,1,0]
rot3=[2,5,8,1,4,7,0,3,6]


rot4=[0,1,2,3]
rot5=[2,0,3,1]
rot6=[3,2,1,0]
rot7=[1,3,0,2]

rot8=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15"]
rot9=["12","08","04","00","13","09","05","01","14","10","06","02","15","11","07","03"]
rot10=["15","14","13","12","11","10","09","08","07","06","05","04","03","02","01","00"]
rot11=["03","07","11","15","02","06","10","14","01","05","09","13","00","04","08","12"]

rot12=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"]

#rot13=["24","20","15","10","05","00","23","19","14","09","04","22","18","13","08","03","17","12","07","02","21","16","11","06","01"]
rot13=["20","15","10","05","00","21","16","11","06","01","22","17","12","07","02","23","18","13","08","03","24","19","14","09","04"]
rot14=["24","23","22","21","20","19","18","17","16","15","14","13","12","11","10","09","08","07","06","05","04","03","02","01","00"]
rot15=["04","09","14","19","24","03","08","13","18","23","02","07","12","17","22","01","06","11","16","21","00","05","10","15","20"]

"""
def split(seq,size):
    x=[]
    y=[]
    z=int(len(seq)/size)
    for j in range(z):
        for i in range(size):
            print(i*z)
            x.append(seq[i*z+j])
        y.append(x)
        x=[]
    print(y)
"""

def divide(seq,size):
    x=[]
    y=[]
    for i in range(size):
        x.append([])
        if i == size :
            x=[]
    #print(x)
    return x

def insert(seq,tab,size):
    z=0
    j=0
    while j < size-1:
        for i in range(len(tab)):
            if z == size:
                z -= size
                j+=1
            z+=1
            tab[j].append(seq[j*size+i])
            #print(tab)
    return tab


tab=divide(rot0,3)
rot0_divided=insert(rot0,tab,3)
tab=divide(rot1,3)
rot1_divided=insert(rot1,tab,3)
tab=divide(rot2,3)
rot2_divided=insert(rot2,tab,3)
tab=divide(rot3,3)
rot3_divided=insert(rot3,tab,3)

tab=divide(rot4,2)
rot4_divided=insert(rot4,tab,2)
tab=divide(rot5,2)
rot5_divided=insert(rot5,tab,2)
tab=divide(rot6,2)
rot6_divided=insert(rot6,tab,2)
tab=divide(rot7,2)
rot7_divided=insert(rot7,tab,2)

tab=divide(rot8,4)
rot8_divided=insert(rot8,tab,4)
tab=divide(rot9,4)
rot9_divided=insert(rot9,tab,4)
tab=divide(rot10,4)
rot10_divided=insert(rot10,tab,4)
tab=divide(rot11,4)
rot11_divided=insert(rot11,tab,4)

tab=divide(rot12,5)
rot12_divided=insert(rot12,tab,5)
tab=divide(rot13,5)
rot13_divided=insert(rot13,tab,5)
tab=divide(rot14,5)
rot14_divided=insert(rot14,tab,5)
tab=divide(rot15,5)
rot15_divided=insert(rot15,tab,5)
#split(rot1,3)
"""
print(rot8_divided)
print(rot9_divided)
print(rot10_divided)
print(rot11_divided)
"""
x="        "

print("rot0:",x,"rot1:",x,"rot2:",x,"rot3: ")
for i in range(3):
    print("    {0}      {1}      {2}      {3}".format(rot0_divided[i],rot1_divided[i],rot2_divided[i],rot3_divided[i]))

print("\n")
x="    "
print("rot4:",x,"rot5:",x,"rot6:",x,"rot7: ")
for i in range(2):
    print("    {0}     {1}     {2}     {3}".format(rot4_divided[i],rot5_divided[i],rot6_divided[i],rot7_divided[i]))

print("\n")
x="                       "
print("rot8:",x,"rot9:",x,"rot10:",x,"rot11: ")
for i in range(4):
    print("    {0}      {1}       {2}       {3}".format(rot8_divided[i],rot9_divided[i],rot10_divided[i],rot11_divided[i]))

print("\n")
x="                            "
print("rot12:",x,"rot13:",x,"rot14:",x,"rot15: ")
for i in range(5):
    print("     {0}      {1}      {2}      {3}".format(rot12_divided[i],rot13_divided[i],rot14_divided[i],rot15_divided[i]))
