tested =[]
# n%2=0
paire = [2,4,6,8,10,12,14]
# n%2 = 1
impaire = [1,3,5,7,9,11,13]
# 2^m=n : A
paire_indef_div=[2,4,8,16]
# n/2 = impaire : B
paire_def_div=[6,10,12,14]
# 3n +1 = 2^m = A : C (ex: 5*3+1=16=2^4=>A)
impaire_indef_div=[1,5]

# 3n+1 != 2^m : D (ex: 3 : 3*3+1 = 10; 10/2 = 5 ; 5 impaire donc non indefiniment divisible)
impaire_def_div=[3,7,9,11,13]


file = open("tested.txt","w")
value = int(file.readlines())
x = value
y = 0

for y in range(x):
    if 2^y == x :
        n = y
print("value = 2^n avec n =",n)

while x < 2 * value:
    flag1 = 0
    if x % 2 = 0 :
        paire = paire + x
        for i in range(n):
            if x == j^n :
                flag1 = 1

        if flag1 == 1 :
            paire_indef_div = paire_indef_div + x
        else :
            paire_def_div = paire_def_div + x
    else :
        impaire = impaire + x
        if x*3+1 =
