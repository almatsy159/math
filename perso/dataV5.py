import tkinter as tk

fen=tk.Tk()
frame=tk.Frame()
h=500
w=500
canvas=tk.Canvas(frame,height=h,width=w)

canvas.create_line(0,w,50,w-50,fill="blue")
x_init=50
y_init=50
U=50
def constante(x,U):
    x=x+U
    return x
def draw_data(data):
    print(data)
    x0=x_init
    y0=y_init
    compteur_1=0
    compteur_0=0
    for i in range(len(data)):

        nom="p"+ str(i)
        if data[i]=="0":
            compteur_0+=1
            x1=x0
            y1=y1+U
        else :
            compteur_1+=1
            x1=x0+U
            y1=y0
        A=x0,y0
        B=x1,y1

        color ="black"
        nom=canvas.create_line(A,B,fill=color)
        print (nom,":",A,B)
        x0=x1
        y0=y1

draw_data("1001")

canvas.pack()
frame.pack()
fen.mainloop()
