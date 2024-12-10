#coding:utf-8

"""

    Returns:NOT FINISHED
        _type_:Need to display image in tk canvas ! _
"""
import tkinter as tk
import tkinter.filedialog as fd

log=[]
class Application(tk.Frame):
    elements=[]

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    """def logs(self,x):
        Application.log.append(x)
        print(Application.log)"""

    def create_widgets(self):

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.frame=tk.Frame(self)
        """option frame tk"""
        self.frame["bg"]="white"
        #self.frame["command"]=self.objets_frame
        self.frame["height"]=400
        self.frame["width"]=800
        self.frame.pack(side="left")
        """
        self.can=tk.Canvas(self.frame,height="400",width="400",bg="black")
        self.can.pack()

    def draw_rect(self):
        self.logs("rect")
        self.can.create_rectangle(10,10,200,200,fill="blue")

    def draw_line(self):
        self.logs("line")
        self.can.create_line(50,150,150,50,fill="red")

    def draw_point(self):
        self.logs("point")
        self.can.create_line(5,5,10,10,fill="white")
        self.can.create_line(10,5,5,10,fill="white")
        """



    def say_hi(self):
        print("hi there, everyone!")

    def update_label(self,*args):
        var_label2.set(var_entry.get())


root = tk.Tk()
menu=tk.Menu(root)
def logs(x):
    log.append(x)
    print(log)

def draw_rect():
    logs("rect")
    can.create_rectangle(10,10,200,200,fill="blue")

def draw_line():
    logs("line")
    can.create_line(50,150,150,50,fill="red")

def draw_point():
    logs("point")
    can.create_line(5,5,10,10,fill="white")
    can.create_line(10,5,5,10,fill="white")


def ouvrir():
    f=fd.askopenfilename(title="Ouvrir un fichier",filetypes=[('PNG files','.png')])
    print(f)

def saveas():
    f=fd.asksaveasfile(title="Enregistrer sous … un fichier",filetypes=[('PNG files','.png')])
    print(f.name)

app = Application(master=root)
can=tk.Canvas(app.frame,height="400",width="400",bg="black")
can.pack()
menufichier = tk.Menu(menu,tearoff=0)
menu.add_cascade(label="Fichier", menu=menufichier)
menuoutils = tk.Menu(menu,tearoff=0)
menu.add_cascade(label= "Outils", menu=menuoutils)

menufichier.add_command(label="Enregistrer")
menufichier.add_command(label="Enregistrer sous",command=saveas)
menufichier.add_command(label="Ouvrir", command=ouvrir)
menufichier.add_command(label="Quitter", command=root.destroy)

menuoutils.add_command(label="Rect",command=draw_rect)
menuoutils.add_command(label="Line",command=draw_line)
menuoutils.add_command(label="Point", command=draw_point)
menuoutils.add_command(label="Del")

def left_click(event):
    X = event.x
    Y = event.y
    print(X,Y)
    return X,Y

def choose_pos():
    X1=can.bind('<Button-1>',left_click)
    return X1


root.config(menu=menu)

app.mainloop()
