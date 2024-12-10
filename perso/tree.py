import tkinter as tk

class Tree(tk.Frame):

    #elements=[]
    data=""
    nb_bit=0
    x=4
    y=4
    xmax=20
    ymax=20
    U=50
    def __init__(self, master=None,data=""):
        super().__init__(master)
        self.master = master
        self["height"]=700
        self["width"]=700
        self["bg"]="black"
        self.sub_win=tk.Tk()
        self.frame=tk.Frame(self.sub_win,height="600",width="600",bg="red")
        self.frame.grid()
        self.data = Tree.data
        self.grid(stick="E")
        #self.draw_grid(Tree.U,Tree.U)
        self.create_widgets()


    def create_widgets(self):

        self.zero = tk.Button(self)
        self.un = tk.Button(self)
        self.un["text"]=0
        self.zero["text"]=1
        self.un["command"]=self.trace_1
        self.zero["command"]=self.trace_0

        self.var_label=tk.StringVar()
        self.var_label.trace("w",self.update_label)
        self.label=tk.Label(self,textvariable=Tree.data)

        #self.label.grid(sticky="S")
        self.zero.grid(column=0,rows=1,sticky="W")
        self.un.grid(column=0,rows=1,sticky="W")


    def update_label(*args):
        var_label.set(Tree.data.get())

    def trace_0(self):
        Tree.data+="0"
        nom="c"+str(Tree.nb_bit)
        self.nom=tk.Canvas(self.frame,height=Tree.U,width=Tree.U,bg="blue")
        self.nom.create_line(0,Tree.U,Tree.U,0,fill="white")
        Tree.nb_bit+=1
        self.afficher()
        self.nom.grid(column=Tree.nb_bit,rows=1)

    def trace_1(self):
        Tree.data+="1"
        nom="c"+str(Tree.nb_bit)
        self.nom=tk.Canvas(self.frame,height=Tree.U,width=Tree.U,bg='green')
        self.nom.create_line(0,Tree.U,0,Tree.U,fill="black")
        Tree.nb_bit+=1
        self.nom.grid(column=Tree.nb_bit,rows=1)
        self.afficher()

    def afficher(self):
        print("Data Tree ",self,":",Tree.data)
    """
    def draw_grid(self,x,y):
        for i in range(Tree.x):
            for j in range(Tree.y):
                nom="canvas"+str(i)+str(j)
                self.nom=tk.Canvas(self,height=Tree.U,width=Tree.U,bg="black")
                self.nom.grid()
                """
root=tk.Tk()
t1=Tree(master=root)
root.mainloop()
