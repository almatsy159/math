import tkinter as tk
import time

data="11100011"
def generate(x):
    list=[]
    for i in range(2**x):
        print("bin de ",i,":",bin(i))

        #if len(bin(i))-2 == x:
        list.append(str(bin(i)[2:]))
    return list
x=len(data)
possibilities=generate(x)
print(possibilities)

#data="101100001111000000000000000000000000001111111111111111111111111111111"
#possibilities=["1111","1110","1101","1100","1011","1010","1001","1000","0111","0110","0101","0100","0011","0010","0001","0000"]
root=tk.Tk()
#frame=tk.Frame(root)
u=10
ku=4
U=u*ku
kx=1
Ux=U*kx
ky=1
Uy=U*ky
"""
def count_possibilities(x):
    if x is str():
        return 2**len(x)
    return 2**x
"""

h = 2*Uy*len(data)
w = Ux*len(data)
while h > 750 or w > 750:
    print("ku:",ku)
    print("ky",ky)
    print("kx:",kx)
    print("h:",h)
    print("w:",w)
    if h > 750 and w > 750:
        print("both!")
        ku=ku/2
        U=u*ku
        Uy = U*ky
        Ux= U*kx
        h = 2*Uy*len(data)
        w = Ux*len(data)
    else:
        print("just h")
        if h > 750:
            ky=ky/2
            Uy=U*ky
            h = 2*Uy*len(data)
        else :
            print("just w")
            kx=kx/2
            Ux=U*kx
            w = Ux*len(data)

frame=tk.Frame(root,height=800,width=800)


canvas=tk.Canvas(frame,height=h,width=w,bg="light blue")




x_init=0
y_init=h//2


canvas.create_line(0,y_init,U,y_init,fill="green")
canvas.create_line(U,y_init,w,y_init,fill="light green")
def f(x):
    y=x
    return y
def g(x):
    y=-f(x)
    return y

    """
def generate_possibilities(x):
    univers=[0,1]

    possibilities=[]
    for i in range(x):

        for j in range(x):
            data.append(1)
        possibilities.append([data])
        """
def draw_data(data):
    print(data)
    x0=x_init
    y0=y_init
    compteur_1=0
    compteur_0=0
    for i in range(len(data)):

        if data[i]=="0":

            nom="p"+ str(i)
            x1=x0+(U*i)
            y1=y0
            x2=x1+U
            y2=y0+f(U)
            A=x1,y1
            B=x2,y2
            if draw_tree ==True:
                if y1<y2 and y1<y_init:
                    color = "purple"
                else :
                    color = "blue"
            else :
                color = "black"
            nom = canvas.create_line(A,B,fill=color)

        else:
            nom="p"+ str(i)
            x1=x0+(U*i)
            y1=y0
            x2=x1+U
            y2=y0+g(U)
            A=x1,y1
            B=x2,y2
            if draw_tree ==True:
                if y1>y2 and y1>y_init:
                    color = "orange"
                else :
                    color = "red"
            else:
                color ="black"
            nom=canvas.create_line(A,B,fill=color)
        compteur_1+=1
        y0=y2
        compteur_0+=1

def draw_WholeTree(possibilities):
    for item in possibilities:
        draw_data(item)
        print(item)


canvas.pack()

frame.pack()
draw_tree = True
draw_WholeTree(possibilities)
draw_tree = False
draw_data(data)

root.mainloop()
