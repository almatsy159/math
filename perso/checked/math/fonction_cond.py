import sys 

print(sys.argv)

def calc1(f1,f2,a):
    if a == 0:
        y=eval(f1)
        return y
    elif a ==1:
        y=eval(f2)
        return y
    else :
        return "error a not bool(0 or 1)"


def write_formula(f1,f2,a,b):
    y="({0}**{1})*({2}**{3})".format(f1,a,f2,b)
    #print(y)
    return y

def non_lambda(a):
    if a==0 :
        return 1
    elif a==1 :
        return 0
    else : 
        print("not 0 or 1")
        return "error"

f1="k"
f2="(-k)"
a=input("write a(0 or 1) : ")
a=int(a)
b=non_lambda(a)
y=write_formula(f1,f2,a,b)
k=5
print("y:{}".format(y))
print(eval(y))
