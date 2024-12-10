# can't be executed rn ...
class expression():
    def __init__(self,name,exp):
        self.exp=exp
        self.name=name

    def calc(self,x):
        self.result=eval(self.exp)
        print(self.name,": ",self.exp," = ",self.result," avec x=",x)

class def_var(expression):
    def __init__(self):
        try:
            eval(expression.exp)
        
f=expression("f","(x**2)")
g=expression("g","(x**(-2))")
osef=3
A=expression("A","(x<osef)")
B=expression("B","(x>=osef)")
x=4
f.calc(x)
g.calc(x)
A.calc(x)
B.calc(x)

k1=expression("k1","({0}**{1})".format(f.exp,A.exp))
k2=expression("k2","({0}**{1})".format(g.exp,B.exp))
k1.calc(x)
k2.calc(x)
k=expression("k","({0}**{1})*({2}**{3})".format(f.exp,A.exp,g.exp,B.exp))
k.calc(x)
