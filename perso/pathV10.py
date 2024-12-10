import tkinter as tk
import f_x
win=tk.Tk()
frame=tk.Frame(win)
data="101100"

class Create_DataTree():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.root=self.x,self.y

class Tree(tk.Frame):
        U=50

        def __init__(self,data, master=None):
            super().__init__(master)
            self.master = master
            self.master.pack()
            self.data = data
            self.create_canvas(self.data)
            self.pack()


        def create_canvas(self,data):

            #h=2.81*Tree.U*len(data)
            #w=len(data)*Tree.U+(2*Tree.U)
            h=700
            w=700
            self.canvas = tk.Canvas(self,height=h,width=w,bg="black")
            #self.label = tk.Label(self.canvas)
            #self.label["text"]=data

            self.canvas.create_line(0,h/2,w,h/2,fill="red")
            osef=len(data)
            for i in range(len(data)):
                x=Tree.U*i
                y=f_x.premier(x,1,h/2)
                y2=y-Tree.U
                self.canvas.create_line(x,y,x+(Tree.U*i),w/2,fill="green")
                for j in range(len(data)-i):
                    self.canvas.create_line(x+(Tree.U*(j*2)),h-y,x+Tree.U*((j*2)+1),h-y-Tree.U,fill="pink")
                y2=y+Tree.U
                y=f_x.premier(-x,1,h/2)
                y2=y+Tree.U
                self.canvas.create_line(x,y,x+Tree.U+((i-1)*Tree.U),y2+((i-1)*Tree.U),fill="blue")
                self.canvas.create_line(x,h-y,x+Tree.U,h-y+Tree.U,fill="purple")
            self.canvas.pack()

data_tree=Tree(data,master=frame)

data_tree.mainloop()
