# be careful super slow one !!

import tkinter
import math
main = tkinter.Tk()
frame = tkinter.Frame(main)
h=700
w=1400
pasx=2
pasy=1
can = tkinter.Canvas(frame,height=h,width=w)


def hexa(x,d=0):
    if x > 9:
        if x == 10 :
            x = "a"
        elif x == 11 :
            x = "b"
        elif x == 12 :
            x = "c"
        elif x == 13 :
            x = "d"
        elif x == 14 :
            x = "e"
        elif x == 15 :
            x = "f"
    else :
        x = str(x)
    return x
"""
def color_used(r,g,b):
    liste=["r","g","b"]

    r=0,0
    g=0,0
    b=0,0
    #for k in liste:
"""
def color_grey(i,j):
    k = i*j
    c=hexa(k)
    color = "#" + c + c + c + c + c + c
    return color

def color(x,y,z):
    #colors = ["00","3f,7e","ff"]
    colors2=["33","66","99","cc"]
    colors=[]
    for i in range(256):
        dizaine = 0
        osef = i
        while osef > 15 :
            osef -= 16
            dizaine +=1
        colors.append(str(hexa(dizaine))+str(hexa(osef)))
    if x == 0 and y == 0 :
        print(colors)
    r = colors[x]
    b = colors[y]
    #print("i = ",i,"; j = ",j,"; i*j/2 =",int(math.floor(i*j/2)))
    g = colors[z]
    color = "#" + r + g + b
    return color

def draw():
    comptx = 0
    compty = 0
    for i in range(255):
        for j in range(255):
            #for k in range(3):
            for k in range(255):
                color_used = color(i,j,k)
                can.create_rectangle(i*pasx,j*pasy,(i+1)*pasx,(j+1)*pasy,fill = color_used)

        comptx += 1
        print("x:",comptx,"; y :",compty)
draw()


#print("hexa de 15 :",hexa(15))
#print("hexa de 8 :",hexa(8))

can.pack()
frame.pack()
main.mainloop()
