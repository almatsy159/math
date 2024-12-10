from tkinter import *
import time

fen=Tk()
frame=Frame(fen)
w=300
h=300
pas=30
#k_1=[1.1,1.1,1.1,1.1]
#k_2=[1.1,1.2,1.1,0.9]
k_1=[1]
k_2=[1]

canvas=Canvas(frame,height=h,width=w,bg="white")
def trace_line(origine,point,color):
    canvas.create_line(origine[0],origine[1],point[0],point[1],fill=color)
    canvas.pack()

def object_courbe_v1(pas):
    for i in range(11):
        origine=0,i*pas
        point=w-i*pas,0
        trace_line(origine,point,"blue")

def object_courbe_v2(pas):
    for i in range(11):
        origine=w,i*pas
        point=w-i*pas,h
        trace_line(origine,point,"blue")

def object_courbe_v3(pas):
    for i in range(11):
        origine=i*pas,0
        point=w,i*pas
        #point=h-i*pas,i*pas
        trace_line(origine,point,"blue")

def object_courbe_v4(pas):
    for i in range(11):
        origine=i*pas,h
        point=0,i*pas
        trace_line(origine,point,"blue")
#object_courbe_v4(pas)
#object_courbe_v3(pas)
#object_courbe_v2(pas)
A=150,100
B=100,200
C=200,200
D=150,150
E=80,50

points=[A,B,C,D]
frame.pack()
vol1=[A,B,C,D,E]
"""
def mvt(nom,I,fct):
    pos_t=[nom]
    for i in range(I[0],I[1]):
        "y"+str(i) = fct(i)
        osef=i,"y"+str(i)
        pos_t.append([osef])
    return pos_t
"""
P1=1,1
P3=w-1,h-1
P5=1,h-1
P7=w-1,1

P2=25,25
P4=w-25,h-25
P6=w-25,25
P8=25,h-25
aire1=[P1,P3,P5,P7]
volx=[P1,P2,P3,P4,P5,P6,P7,P8]

def change_value(A,k1,k2):
    B=A[0]*k1,A[1]*k2
    return B

print("A avant :",A)
A=change_value(A,0.5,2)
print("A apres :",A)
canvas=Canvas(frame,height=w,width=h,bg="black")

def draw_volume(points,nb=0):
    colors=["red","blue","green","white"]
    #canvas=Canvas(frame,height=w,width=h,bg="black")
    while nb > len(colors):
        nb=nb//len(colors)

    canvas.pack(side="left")
    for origine in points:
        for point in points:
            canvas.create_line(origine[0],origine[1],point[0],point[1],fill=colors[nb])
            #trace_line(origine,point,colors[nb])
            #trace_line(origine,points,colors[nb])???
            #canvas.create_line(origine[0]-i*50,origine[1]-i*50,point[0]+i*50,point[1]+i*50,fill=colors[i])

draw_volume(volx,2)

def draw_volume2(origines,points,nb=0):
    colors=["white","red","blue","green"]
    while nb > len(colors):
        nb//len(color)

    for origine in origines:
        for point in points:
            print("o : ",origine," p :",point)
            canvas.create_line(origine[0],origine[1],point[0],point[1],fill=colors[nb])
            canvas.pack()

def volume_mvt(points,k_1,k_2):
    compt=0
    for i in range(len(k_1)):
        canvas=Canvas(frame,height=w,width=h,bg="black")
        nom="vol"+str(i)
        nom=draw_volume(points,0)
        """
        courbe1=object_courbe_v1(25)
        courbe2=object_courbe_v2(25)
        courbe3=object_courbe_v4(pas)
        courbe4=object_courbe_v3(pas)
        """
        for point in points:
            print("points",point,"canvas",i,":",point)
            point=change_value(point,k_1[i],k_2[i])
            compt+=1
            points[i]=point
        time.sleep(0.05)

frame.pack()
volume_mvt(points,k_1,k_2)
pas = 50

def axe_x(pas,w):
    axe=[]
    for i in range((w//pas)+1):
        nom="x"+str(i)
        nom = i*pas,0
        axe+=[nom]

    return axe

def axe_y(pas,h):
    axe=[]
    for i in range((h//pas)+1):
        nom="x"+str(i)
        nom = 0,i*pas
        axe+=[nom]
    return axe

origine=0,0
#def origine
axe1=axe_x(pas,w)
axe2=axe_y(pas,h)
#repere=[origine],[axe_x(pas,w)],[axe_y(pas,h)]
#draw_volume(aire1,1)
#draw_volume(points)
#draw_volume(axe_x(pas,w)+axe_y(pas,h))
#draw_volume2(axe_x(pas,w),axe_y(pas,h))
"""
vol3=[]
for i in range((w//pas)+1):
    A=0,i*pas
    B=w-i*pas,0
    vol3=[A][B]
    draw_volume(A,vol3)
def extraction(liste):
    osef=[]
    cmpt=0
    for i in liste:
        nom=i[cmpt],i[cmpt+1]
        osef+=nom
        cmpt+=1
    print(osef)
    return osef
"""

fen.mainloop()

"""
def point_dans_repere(nom,x,y,unite):
    nom=x*unite,y*unite
    return nom

def point(nom,numero,x,y,unite=1):
    nom_du_point=nom+str(numero)
    point_dans_repere(nom_du_point,x,y,unite)

def volume(points):
    for i in range(len(points)):
        nom="P"+str(i)
        valeur=point(nom,i,points[i][0],point[i][1])
"""
