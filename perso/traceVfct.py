import tkinter as tk
root=tk.Tk()
c=25
t=20

frame=tk.Frame(root,height=(c*t),width=(c*t))
frame.pack()

for i in range(t):
    for j in range(t):
        canvas=tk.Canvas(frame)
        tracer=create_line(canvas,0,0,i,j,color="red")
        tracer.pack()
        j+=1
    i+=1
tracer=canvas.create_line(frame,10*25,0,10*25,10*25,color="black")

def tracer(master,x0,y0,x1,y1):
    tk.Draw_line(master,x0,y0,x1,y1)
root.mainloop()
