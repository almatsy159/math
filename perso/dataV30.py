import tkinter as tk
import time

root=tk.Tk()
frame=tk.Frame(root,height="700",width="700")

class Tree(tk.Frame):
    #data="1011" #for data in possibilities => data**2
    possibilities=["1111","1110","1101","1100","1011","1010","1001","1000","0111","0110","0101","0100","0011","0010","0001","0000"]
    U=50
    #ajouter data
    def __init__(self,h,w,master=None,data=""):
        self.master=master
        super().__init__()
        self.data_in=data
        if self.data_in=="":
            self.data_in=Tree.possibilities

        self.h=h
        self.w=w
        self.canvas=tk.Canvas(self,height=h,width=w)
        self.x_init=0
        self.y_init=self.h//2

        self.pack()
        self.canvas.create_line(0,y_init,x_init,y_init,fill="green")
        self.canvas.pack()
        self.x0=self.x_init
        self.y0=self.y_init
        self.compteur_1=0
        self.compteur_0=0
        self.draw_WholeTree(possibilities)
        self.mainloop()

    def f(self,x):
        y=x
        return y

    def g(self,x):
        y=-f(x)
        return y


    def draw_data(self,data):
        for i in range(len(data)):

            if self.data[i]=="1":

                nom="p"+ str(i)
                x1=x0+(U*i)
                y1=y0
                x2=x1+U
                y2=y0+f(U)
                A=x1,y1
                B=x2,y2
                nom = canvas.create_line(A,B,fill="blue")

            else:
                nom="p"+ str(i)
                x1=x0+(U*i)
                y1=y0
                x2=x1+U
                y2=y0+g(U)
                A=x1,y1
                B=x2,y2
                nom=canvas.create_line(A,B,fill="red")
            compteur_1+=1
            y0=y2
            compteur_0+=1

    def draw_WholeTree(possibilities):
        for item in possibilities:
            draw_data(item)

t1=Tree(frame,200,200)
