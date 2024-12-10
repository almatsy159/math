class A:
     t=input("tapez un nombre")
     t=int(t)
     def f(self,x):
             y=x*2
             return y
     def __init__(self,x):
             self.x=x
             self.y=self.f(self.x)
             self.z=self.g(self.y,self.t)
     def g(self,x,y):
             if y%2 == 0:
                     z = "pair"
             else :
                     z = "impair"
             return (x,z)

a=A(10)
print("class",A(10))
print("objet",a)
print("class without init",A)
print("a.x = ",a.x)
print("a.y = ",a.y)
print("a.z = ",a.z)
