import tkinter as tk
x0=0
x1=50
x2=100
Xi=[]
u=10
d=20
a=1
h=500

def premier(x,a,b):
    return a*x+b

y0=premier(x0,1,h/2)

data="000000000"

def draw(bit,x1,pas):#a = 1/-1

    h=pas
    w=pas/2
    x0=x1-pas
    root=tk.Tk()#exteriorisé element tk !!
    canvas=tk.Canvas(height=h,width=w,bg="black")
    if bit==0:
        canvas.create_line(x0,premier(x0,1,h/2),x1,premier(x1,1,h/2),fill="blue")
        canvas.create_line(x0,premier(x0,-1,h/2),x1,premier(x1,-1,h/2),fill="grey")
    else:#pas encore traité
        x0,premier(x0,-1,h/2),x2,g(x2)
    canvas.pack()
    root.mainloop()

for i in range(20):
    Xi.append(20*i)
    nom="y"+str(i)
    nom=premier(Xi[i],1,(h/2)-u*i)
    print("x=",i," : f(x)=",nom)
    nom=-nom
    print("x=",i," : g(x)=",nom)


draw(0,100,100)
