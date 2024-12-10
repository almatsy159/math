

class matrice :
    #sequence=[]
    id=0
    def __init__(self,name,ref=None,*args):
        self.id=matrice.id
        matrice.id += 1
        self.sequence=[]
        self.ref=ref
        self.part_num_name= ""
        self.dim = 0
        #print(args)
        self.row = args[0]
        self.col = args[1]
        if len(args) > 1:
            self.others = args[2:]
        for i in args :
            self.part_num_name +="_"+ str(i)
            self.dim += 1
        self.part_alpha_name=name
        self.name = self.part_alpha_name + self.part_num_name
        #print("obj:",self,"prop : name =>",self.name," ; dim =>",self.dim)

    def emptying(self):
        self.sequence=[]

    def fill(self,sequence):
        for i in sequence:
            self.sequence.append(i)

    def split_row(self,size):
        y=[]
        x=[]
        z=1
        for i in range(len(self.sequence)):
            #print("z:",z)
            x.append(self.sequence[i])
            if z == size:
                #print("x :",x)
                y.append(x)
                x=[]
                z=z-size
            z += 1
        #print("y:",y)
        self.sequence=y

    def split_col(self,size):
        i=0
        x=[]
        y=[]
        j=0
        while j < size:
            while i < len(self.sequence):
                x.append(self.sequence[i+j])
                i += size
            j +=1
            i=0
            y.append(x)
            x=[]
        #print(y)
        self.sequence = y

    def unsplit(self):
        x=[]
        for i in self.sequence:
            for j in i:
                x.append(j)
        self.sequence = x
#creation des matrices
m33=matrice("m","X",3,3)
m23=matrice("m","X",2,3)
m32=matrice("m","X",3,2)

sequence=[0,1,2,3,4,5,6,7,8]
sequence2=[9,10,11,12,13,14]

def fill(sequence,matrice):
    for i in sequence :
        matrice.sequence.append(i)
"""
def split(matrice):
    x=[]
    for i in range(len(matrice.name)):
        temp=""
        if matrice.name[i] == "_":
            for j in range(len(matrice.name)-i):
                if int(matrice.name[j+i]):
                    temp = "dim"+str(i)
                    temp = i
                else :
                    break
        x.append(temp)
    matrice.sequence
    return x
"""
def split_row(matrice,size):
    y=[]
    x=[]
    z=1
    for i in range(len(matrice.sequence)):
        #print("z:",z)
        x.append(matrice.sequence[i])
        if z == size:
            #print("x :",x)
            y.append(x)
            x=[]
            z=z-size
        z += 1
    #print("y:",y)
    return y

"""
def split_col(matrice,size):
    y=[]
    x=[]
    z=1
    for i in range(len(matrice.sequence)-1):
        j=0
        while j < size:
            x.append(matrice.sequence[j+z])
            if z == size:
                print(x)
                y.append(x)
                x=[]
                z=z-size
            j += size
            z += 1
    print(y)
"""
def split_col(matrice,size):
    i=0
    x=[]
    y=[]
    j=0
    while j < size:
        while i < len(matrice.sequence):
            x.append(matrice.sequence[i+j])
            i += size
        j +=1
        i=0
        y.append(x)
        x=[]
    #print(y)
    return y

def unsplit(matrice):
    x=[]
    for i in matrice:
        for j in i:
            x.append(j)
    return x

# attribution des sequences
#fill(sequence,m33)
m33.fill(sequence)
#fill(sequence2,m23)
#print(m33.sequence)
m23.fill(sequence2)
#print(m23.sequence)
#fill(sequence2,m32)
m32.fill(sequence2)

#print("sequence de m33 :",m33.sequence)
m33.split_row(3)
#print(m33.sequence)
#m33.unsplit()
m33.emptying()
print(m33.sequence)
m33.fill(sequence)
print(m33.sequence)
m33.split_col(3)
print(m33.sequence)

#splited_in_row_m33=split_row(m33,3)
#splited_in_col_m33=split_col(m33,3)
#print(splited_in_row_m33)
#print(splited_in_col_m33)

m33.unsplit()
#unsplited_m33_col=unsplit(splited_in_col_m33)
#print(unsplited_m33_col)
print(m33.sequence)
#rot multiple de m33

#m33.split_col(3),m33.unsplit()
#print(m33.sequence)
"""
m33.sequence.reverse()
m33.split_row(3),m33.unsplit()
print(m33.sequence)
m33.split_col(3),m33.unsplit()
print(m33.sequence)
m33.sequence.reverse()
m33.split_col(3),m33.unsplit()
print(m33.sequence)
"""

m23.split_row(3)
m32.split_row(2)
#splited_in_row_m23=split_row(m23,3)
#splited_in_row_m32=split_row(m32,2)
"""
print("m(2,3)",m23.sequence)
print("m(3,2)",m32.sequence)
"""
m32.emptying()
m23.emptying()
fill(sequence2,m23)
fill(sequence2,m32)
m32.split_col(3)
m23.split_col(2)
#splited_in_col_m32=split_col(m32,3)
#splited_in_col_m23=split_col(m23,2)
"""
print("m(3,2)",m32.sequence)
print("m(2,3)",m23.sequence)


print("m(2,3)",splited_in_row_m23)
print("m(3,2)",splited_in_row_m32)
print("m(3,2)",splited_in_col_m32)
print("m(3,2)",splited_in_col_m23)
"""
