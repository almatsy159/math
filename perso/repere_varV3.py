from tkinter import *
A=0,0
h=200
w=200
B=h,w
A1=0,w
A2=h,0
liste_origine=[A,B,A1,A2]
colors=["blue","orange","green","yellow","red","purple"]

C=150,150
D=50,50
E=150,50
F=50,150
G=100,100
points=[C,D,E,F,G]

origine=A
point=C
fenetre=Tk()
frame=Frame(fenetre)
canvas=Canvas(frame,height="400",width="400",bg="black")
#canvas1=Canvas(canvas,height="200",width="200",bg="white")
#canvas2=Canvas(canvas,height="100",width="100",bg="grey")
frame.pack()
#canvas1.pack()
#canvas2.pack()
canvas.pack()
"""
def constante(x1,y,x2):
    A=x1,y
    B=x2,y
    canvas.create_line(A[0],A[1],B[0],A[1])
constante(0,150,200)
"""

def trace_line(origine,point,color):
    canvas.create_line(origine[0],origine[1],point[0],point[1],fill=color)


def delta(x_init,x_final):
    return abs(x_final-x_init)
print(delta(4,5))
print(delta(5,4))

def change_sens(x):
    return -x

osef=150,100
retour=change_sens(osef[0])

print("retour:",retour)
#for i in range(nb):
#nom="c"+str(i)
for origine in liste_origine:
    for point in points:
        trace_line(origine,point,"white")


origine=B

#trace_line(origine,C,"grey")

fenetre.mainloop()
