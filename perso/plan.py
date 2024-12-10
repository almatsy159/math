import tkinter as tk
import tkinter.filedialog as fd

main = tk.Tk()
log=[]
event=[]

def left_click(event):
    X = event.x
    Y = event.y
    print(X,Y)
    return X,Y

def choose_pos():
    X1=can.bind('<Button-1>',left_click)
    return X1

def logs(x):
    log.append(x)
    print(log)

def ouvrir():
    logs("ouvrir")
    f=fd.askopenfilename(title="Ouvrir un fichier",filetypes=[('PNG files','.png')])
    print(f)

def saveas():
    logs(savesas)
    f=fd.asksaveasfile(title="Enregistrer sous … un fichier",filetypes=[('PNG files','.png')])
    print(f.name)

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


frame = tk.Frame(main)
can = tk.Canvas(frame,height="600",width="1200",bg="black")
menu=tk.Menu(main)


frame.pack()
can.pack()

main.config(menu=menu)


menufichier = tk.Menu(menu,tearoff=0)
menu.add_cascade(label="Fichier", menu=menufichier)
menuoutils = tk.Menu(menu,tearoff=0)
menu.add_cascade(label= "Outils", menu=menuoutils)

menufichier.add_command(label="Enregistrer")
menufichier.add_command(label="Enregistrer sous",command=saveas)
menufichier.add_command(label="Ouvrir", command=ouvrir)
menufichier.add_command(label="Quitter", command=main.destroy)

menuoutils.add_command(label="Rect",command=draw_rect)
menuoutils.add_command(label="Line",command=draw_line)
menuoutils.add_command(label="Point", command=draw_point)
menuoutils.add_command(label="Del")

can.bind('<Button-1>',left_click)


main.mainloop()
