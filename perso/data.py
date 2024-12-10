import tkinter as tk
import time
import colorsys
data="1011" #for data in possibilities => data**2
root=tk.Tk()
frame=tk.Frame(root)
canvas=tk.Canvas(frame,height="600",width="600")
x_init=150
y_init=150
U=50
frame.pack()
canvas.pack()
def f(x):
    y=x
    return y
def g(x):
    y=-f(x)
    return y
for i in range(len(data)):

    if data[i]=="1":

        nom="p"+ str(i)
        x=x_init+U*i
        """A=x,f(x)
        B=x+1,f(x+1)"""
        nom=canvas.create_line(x,f(x),x+U,f(x+U),fill="blue")
    else:
        nom="p"+ str(i)
        x=x_init+U*i
        nom=canvas.create_line(x,f(x),x+U,g(x+U),fill="red")






root.mainloop()
