import tkinter as tk

fen=tk.Tk()
frame=tk.Frame(fen)
can=tk.Canvas(frame,height="600",width="600",bg="white")
b=50
a=2
def oui(x):
    y=x
    return y

def fonction_base(x,fct=oui):
    y=fct(x)
    return y

def ax_plusb(x,a=1,b=10):
    y=x*a + b
    return y

def interval(x,y):
    I=x,y
    return I

def trace(I,fct):
    #for i in range(I[0],I[1]):
    print("x :",I[0],"; y:",fct(I[0]))
    print("x :",I[1],"; y:",fct(I[1]))
    can.create_line(I[0],fct(I[0]),I[1],fct(I[1]),fill="green")

def trace2(x_init,pas,fct):

    can.create_line(x_init,fct(x_init),x_init + pas,fct(x_init + pas),fill="purple")

fx_1=fonction_base(100)
print(fx_1)

def second_degres(x,a=1,b=1,c=0):
    y=(a*x*x)+b*x+c
    return y

for i in range(0,100):
    y1=second_degres(i,2,2,2)
    print("x :",i,"; y :",y1)
    y0=second_degres(i-1,2,3,2)
    y1=round(y1/100)
    y0=round(y0/100)
    can.create_line(i,y1,i-1,y0,fill="red")

I=interval(0,20)
for i in range(I[1]):
    pas=10
    trace2(20,10,oui)


fx_2=trace(I,second_degres)

#can.create_line(0,0,100,100,fill="green")
frame.pack()
can.pack()
fen.mainloop()
