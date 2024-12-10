import tkinter as tk

fen=tk.Tk()
frame=tk.Frame()
h=500
w=500
canvas=tk.Canvas(frame,height=h,width=w)

canvas.create_line(0,h,50,h-50,fill="green")
U=50
x_init=0+U
y_init=h-50

def draw_data(data):
    print(data)
    x0=x_init
    y0=y_init
    compteur_1=0
    compteur_0=0
    axe_x=canvas.create_line(U,h-U,len(data)*U+U,h-U,fill="blue")
    axe_y=canvas.create_line(U,h-U,U,h-U-(len(data)*U),fill="red")
    lim_data=canvas.create_line(len(data)*U+U,h-U,U,h-U-(len(data)*U),fill="purple")
    for i in range(len(data)):


        nom="p"+ str(i)
        if data[i]=="0":
            compteur_0+=1
            x1=x0
            y1=y1-U
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
draw_data("10001100")
draw_data("11001011")

canvas.pack()
frame.pack()
fen.mainloop()
