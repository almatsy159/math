import tkinter as tk
root=tk.Tk()
from PIL import Image
import numpy as np

c=18#taille d'une sub
t=30#nombre de sub
h=t*c
w=t*c

frame=tk.Frame(root,height=h,width=w,bg="black")


canvas=tk.Canvas(frame,height=h,width=w,bg="white")

for i in range(t):
    #for j in range(w):
        d=0
        x=i*c
        f=t
        tracer=canvas.create_line(0,x,w,x,fill="orange")
        #tracer=canvas.create_line(0,h,i*c,i,fill="purple")
        #tracer=canvas.create_line(i*c,0,w,h)
        #tracer=canvas.create_line(w,0,i,i*c,fill="grey")
        tracer=canvas.create_line(x,0,x,h,fill="purple")
        #tracer1=canvas.create_line(x,x,h-x,x,fill="blue")
        tracer1=canvas.create_line(x,x,h,x,fill="blue")
        #j+=1


tracer0=canvas.create_line(0,0,w,h,fill="blue")

centreh=h//2
centrew=w//2
#tracer2=canvas.create_line(10,60,centrew,centreh,fill="red")
#tracer3=canvas.create_line(0,50,150,50,fill="green")
#tracer4=canvas.create_line(150,150,0,150)
#tracer5=canvas.create_line(150,50,150,0,fill="pink")
img = PhotoImage(width = canvas_width, height = canvas_height)
"""
img=Image(canvas)
img=np.array(img)
print(img.shape)
img.save('resultat1.jpg')
"""
print(canvas)
canvas.pack()
frame.pack()


root.mainloop()
