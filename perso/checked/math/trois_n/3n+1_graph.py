import tkinter as tk

fen = tk.Tk()
frame = tk.Frame(fen)
h=600
w=1200
graph= tk.Canvas(frame,height=h,width=w,bg="white")


entry = tk.Entry()
axe_y = tk.Canvas(frame,height=h,width = 50,bg="white")
axe_x = tk.Canvas(frame,height= 50,width = w,bg="white")

pas_y = 0
pas_x = 0

y = input("val to test :")

#label1=tk.Label(axe_y,text=y)
def ligne_vert(y,color="black"):
    graph.create_line(0,y,w,y,fill=color)

def ligne_hor(x,color="black"):
    graph.create_line(x,0,x,h,fill=color)

def point(x,y):
    #cross
    delta=5
    graph.create_line(x-delta,y-delta,x+delta,y+delta,fill="red")
    graph.create_line(x-delta,y+delta,x+delta,y-delta,fill="red")

#point(20,20)
#ligne_hor(100)
#ligne_vert(200)
i=0
j=0

def calc(x):
    result=[x]
    while x != 1:
        if x % 2 == 0:
            x = x/2
        else :
            x = x*3 +1
        result.append(x)
    print(result[0],":",result)
    return result


max_result=0
y=int(y)
res=calc(y)
len_nb=len(res)

for i in res:
    if i > max_result:
        max_result=int(i)
print("y_max =",max_result)


passed_value=[]
two_power_x=0
i=0
while i<max_result:
    two_power_x+=1
    i=2**two_power_x
    passed_value.append(i)



pas_y=h/max_result
pas_x=w/len_nb


compt=0
while j < w :
    if compt in passed_value:
        ligne_hor(j,"green")
    else:
        ligne_hor(j)
    j +=pas_x
    compt+=1


compt=0
while i < h :
    if compt in passed_value:
        ligne_vert(i,"purple")
    else :
        ligne_vert(i)
    i +=pas_y
    compt +=1

max = h/pas_y
print("max :",max)
#for i in range(len(passed_value)):
#    ligne_vert(h-(passed_value[i]*pas_y*i),"blue")
print("last power of 2 :",passed_value)
#for j in range(y):
#    res=calc(j)

i=1
j=1

while j <= y:
    print("j=",j)
    res=calc(j)
    if j == y :
        color="blue"
    else:
        if len(res)> len_nb:
            color="red"
        else:
            color="black"
    for i in range(len(res)):
        point(i*pas_x,h-(res[i]*pas_y))
        graph.create_line((i-1)*pas_x,h-(res[i-1]*pas_y),i*pas_x,h-(res[i]*pas_y),fill=color)
    j += 1

frame.pack()
graph.pack()
fen.mainloop()
