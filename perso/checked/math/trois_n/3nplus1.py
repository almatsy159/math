import math
# n%2=0
paire=[]

# n%2=1
impaire=[]

# 2^m=n : A
paire_indef_div=[]

# is_power_of_two = 0 : B
paire_def_div=[]

# 3n +1 = 2^m = A : C (ex: 5*3+1=16=2^4=>A) se retrouve puissance de deux a la prochaine opération
impaire_indef_div=[]

# 3n+1 != 2^m : D (ex: 3 : 3*3+1 = 10; 10/2 = 5 ; 5 impaire donc non indefiniment divisible)
impaire_def_div=[]

values = [9,16,5,6,21,11,18,32,27,41,31,47,71,107,161,121,91,137,103,155,233,175,263,395,593,445,167,251,377,283,425,319,479,719,1079,1619,2429,911,1367,2051,3077,577,433,325,61,23,35,53]

def fois3plus1(x):
    y = x*3+1
    print(x,"*3 +1 =",y)
    return y

def divide_by_two(x):
    y = x /2
    print(x,"/2 =",y)
    return y

def paire(x):
    if x % 2 == 0:
        return 1
    else :
        return 0

def is_power_of_two(x):
    flag = 1
    y=x
    while paire(x/2)==1  and x/2 != 1 :
        flag += 1
        x=x/2
    x = math.floor(x)
    print("nb depart :",y,"; nombre d'arrivée :",x/2)
    if x == 2:
        return 1
    else :
        return 0

def indef_div_by_two(x):
    #uniquement pour pair
    if is_power_of_two(x) == 1:
        return 1
    else :
        return 0

def classify_first_step(x):
    if paire(x) == 1 :
        y=divide_by_two(x)
        if is_power_of_two(y) == 1:
            return "A"
        else :
            return "B"
    else :
        y=fois3plus1(x)
        if is_power_of_two(y) == 1:
            return "C"
        else :
            return "D"

for i in values :
    print("trying :",i)
    osef=classify_first_step(i)
    if osef == "A":
        paire_indef_div.append(i)
        print(osef,":",i,"paire_indef_div :",paire_indef_div,"\n")
    if osef == "B":
        paire_def_div.append(i)
        print(osef,":",i,"paire_def_div : ",paire_def_div,"\n")
    if osef == "C":
        impaire_indef_div.append(i)
        print(osef,":",i,"impaire_indef_div : ",impaire_indef_div,"\n")
    if osef == "D":
        impaire_def_div.append(i)
        print(osef,":",i,"impaire_def_div : ",impaire_def_div,"\n")
