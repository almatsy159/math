from tkinter import *

class volume:
    id=0
    def __init__(self,x,y,z,t,unite=1):   #x,y,z,t sont des distance (interval)
        self.nom= volume.id
        self.unite=unite
        self.x=x
        self.y=y
        self.z=z
        self.t=t
        self.pos_cg=self.x*self.unite,self.y*self.unite,self.z*self.unite,self.t*self.unite
        volume.id +=1

    def draw_vol(self):
        self.fen=Tk()
        self.frame=Frame(self.fen)
        self.canvas=Canvas(self.frame)

    def equation(self,nom,expression,variable):
        nom = expression
        return nom

    def mvt(self,v):
        pass
var1="x"
var2="y"
operator1="="

def test(i,j):
    A=1 if i < j else 0
    return A

eqpression=var1+operator1+var2
x=1

a=test(2,3)
print(a)
#f_de_x=equation("f(x)","y=x","x")

def calcul(equation,valeur):
    x=valeur
    equation
