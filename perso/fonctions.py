import tkinter as tk


def premier(x,a):
    return a*x

def repere():
    U=input("valeur de l'unite (en px pour gui)")
    U=int(U)#def unite

    Int0=input("debut de l'inteval ?")#def interval
    Int1=input("fin de linterval ?")
    Int0=int(Int0)
    Int1=int(Int1)

    if Int0>Int1:
        delta0=Int0-Int1
    else:
        delta0=Int1-Int0

    w=delta0
def hauteur():
    k=input("saisir le coefficient liant x et y : type(ax+b) NB:1 pour un carré")
    k=int(k)
    h=premier(delta0,k)
    centre=h/2,w/2
    """
    return w
def origine(x,U):
    x_ori=input("saisir la position de l'origine (x)" )
    y_ori=input("saisir la position de l'origine (y)" )
    #cf pos frame tk
    y_ori=h-int(y_ori)


def open_win():
    root=tk.Tk()
    frame=tk.Frame(root)
    return frame
def draw_canvas(frame,h,w):
    canvas=tk.Canvas(frame,height="h",width="w")

def repeat(x):
    for i in range(x):
            draw_canvas(frame,h*i,h*i)
def pack_widgets():
    frame.pack()
    window.mainloop()


r1=repere()

window=open_win()
c1=draw_canvas(window,r1,r1(1))
pack_widgets()
