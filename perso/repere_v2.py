import tkinter as tk

fen=tk.Tk()
frame=tk.Frame(fen)
canvas=tk.Canvas(frame)
#c1=tk.Canvas(canvas,height="100",width="100",bg="black")
#c2=tk.Canvas(canvas,height="100",width="100",bg="grey")
def draw(A=(0,0),B=(150,150),nom="c",color="white"):
    nom.create_line(A[0],A[1],B[0],B[1],fill=color)


def n_canvas(n,procedure=None,bg_color="black",fg_color="white"):

    for i in range(n):
        nom="c"+str(i)
        nom=tk.Canvas(canvas,height="100",width="100",bg=bg_color)
        if procedure != None :
            exe=str(procedure)+"()"
            exe
        nom.pack(side="left") #algo de repartition
        A=[0,0]
        B=[100,100]
        draw(A,B,nom,"red")
        for i in range(n):
            A[0]=10*i
            draw(A,B,nom,fg_color)
    return n
nb=n_canvas(2)



n_canvas(4,draw,"purple")
frame.pack()
canvas.pack()
#c1.pack()
#c2.pack()

fen.mainloop()
