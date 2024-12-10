# render seem ok ! =) 
import tkinter
import math
main = tkinter.Tk()
frame = tkinter.Frame(main)
h=700
w=700
pas=50
can = tkinter.Canvas(frame,height=h,width=w)

# hexa moche !!
def hexa(x):
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

def color(i,j,x):
    #colors = ["00","3f,7e","ff"]
    colors=["00","33","66","99","cc","ff"]
    r = colors[j]
    b = colors[i]
    #print("i = ",i,"; j = ",j,"; i*j/2 =",int(math.floor(i*j/2)))
    if x == 0 :
        g = colors[-int(math.floor(i/2*j/2))]
    else:
        g = colors[int(math.floor(i/2*j/2))]
    color = "#" + r + g + b
    return color
def draw(x):
    for i in range(5):
        for j in range(5):
            color_used = color(i,j,x)
            if x == 0 :
                can.create_rectangle(i*pas,j*pas,(i+1)*pas,(j+1)*pas,fill = color_used)
            else :
                can.create_rectangle(i*pas+350,j*pas+350,(i+1)*pas+350,(j+1)*pas+350,fill = color_used)
draw(0)
draw(1)


#print("hexa de 15 :",hexa(15))
#print("hexa de 8 :",hexa(8))

can.pack()
frame.pack()
main.mainloop()
