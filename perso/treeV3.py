import tkinter as tk

class Application(tk.Frame):
    #elements=[]
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def say_hi(self):
        print("hi there, everyone!")

    def create_widgets(self):

        self.hi_there = tk.Button(self)

        self.hi_there["text"] = "Hello World\n(click me)"
        #self.hi_there["command"] = self.say_hi
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.frame=tk.Frame(self)
        """option frame tk"""
        self.frame["bg"]="white"
        #self.frame["command"]=self.objets_frame
        self.frame["height"]=700
        self.frame["width"]=400

        self.frame.pack()

        self.U=5
        self.h=150
        self.w=150
        self.canvas=tk.Canvas(self.frame,height=self.h,width=self.w,bg="white")
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.nbUw=int(self.w//self.U)
        self.nbUh=int(self.h//self.U)
        for i in range(self.nbUw):
            nom="c"+str(i)
            self.nom0=tk.Canvas(self.canvas,bg="blue")
            for j in range(self.nbUh):
                nom1="c"+str(i)+str(j)
                self.nom1=tk.Canvas(self.nom0,height="10",width="10",bg="black")
            #self.nom.grid(rows=i)
                self.nom1.pack(side="left")
            self.nom0.pack()
        self.canvas.pack()

root = tk.Tk()
tree = Application(master=root)
tree.mainloop()
