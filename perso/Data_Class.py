import tkinter as tk


class Data:
    def __init__(self,data="",mode=None):

        self.data = data
        self.mode = mode
        self.root=tk.Tk()
        self.frame=tk.Frame(self.root)
        self.root.mainloop()

    def generate(self,x):
        list=[]
        for i in range(2**x):
            print("bin de ",i,":",bin(i))
            osef=str(bin(i)[2:])
            while len(osef)<len(data):
                osef = "0" + osef
            #if len(bin(i))-2 == x:
            list.append(osef)
        return list

    def f(self,x):
        y=x
        return y
    def g(self,x):
        y=-f(x)
        return y

    def draw_data(self,data):
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
                #color tree

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

    def draw_WholeTree(self,possibilities):
        for item in possibilities:
            draw_data(item)
            print(item)

Data("0001110",1)
