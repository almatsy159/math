import tkinter as tk

fen=tk.Tk()
main=tk.Frame(fen)
h=300
w=300
can=tk.Canvas(main,height=h,width=w)

def rect(x1,y1,x2,y2,color):
    can.create_rectangle(x1,y1,x2,y2,fill=color,width=1)

col1="blue"
col2="red"
col3="green"
x_r1=[100,200]
y_r1=[100,200]
x_r2=[150,250]
y_r2=[150,250]
forme1=[]
forme2=[]
"""
for i in x_r1):
    forme1.append(i)
for j in y_r1:
    forme1.append(i)
"""
def forme_x(xs,ys):
    forme=[]
    for i in xs:
        forme.append(i)
    for j in ys:
        forme.append(i)
    return forme
forme1=forme_x(x_r1,y_r1)
forme2=forme_x(x_r2,y_r2)

"""
def intersection(forme1,forme2):
    for i in range(forme1[0]):
        for j in range(forme1[0]):
"""
grid=[]

for i in range(10):
    for j in range(10):
        grid.append(0)

grid[55]=grid[55]+1
grid[62]=grid[62]+1
grid[62]=grid[62]+1

col_x="black"
def draw_pix(x,y,color):
    rect(x,y,x,y,color)

for i in range(20):
    for j in range(20):
        draw_pix(i,j,col_x)


print(grid)
"""
for i in grid:
    print(type(i))
"""

rect(x_r1[0],y_r1[0],x_r1[1],y_r1[1],col1)
rect(x_r2[0],y_r2[0],x_r2[1],y_r2[1],col2)
rect(150,150,200,200,col3)
rect(10,10,10,10,"purple") #pixel
main.pack()
can.pack()
fen.mainloop()
