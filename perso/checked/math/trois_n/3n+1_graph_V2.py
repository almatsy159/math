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


def ligne_vert(x,color="black"):
    graph.create_line(x,0,x,h,fill=color)

def ligne_hor(y,color="black"):
    graph.create_line(0,y,w,y,fill=color)

def point(x,y):
    #cross
    delta=5
    graph.create_line(x-delta,y-delta,x+delta,y+delta,fill="red")
    graph.create_line(x-delta,y+delta,x+delta,y-delta,fill="red")

#ligne_hor(100,"blue")
#ligne_vert(200,"green")
i=0
j=0

def calc_three_nPlusOne(x):
    result=[x]
    while x != 1:
        if x % 2 == 0:
            x = x/2
        else :
            x = x*3 +1
        result.append(x)
    print(result[0],":",result)
    return result

def max_list(res):
    max_result=0
    for i in res:
        if i > max_result:
            max_result=int(i)
    print("y_max =",max_result)
    return max_result

def power_of_two(x):
    passed_value=[]
    two_power_x=0
    i=0
    while i<x:
        i=2**two_power_x
        two_power_x+=1
        passed_value.append(i)

    return passed_value

def prop(x,y):
    return y/x


y = input("val to test :")
y=int(y)

# calcul des differentes valeurs parcourus avec y
res=calc_three_nPlusOne(y)
# definition du maximum atteind par y
max_res=max_list(res)
# nombre de calcul réalisé
len_nb=len(res)
# interval : 2^n-1 < max_res < 2^n
passed_value=power_of_two(max_res)
print("valeur 2^n passée :",passed_value)
# 1 case correspond a "pas" pixel en x et y
pas_y=prop(max_res,h)
pas_x=prop(len_nb,w)
#print("quadrillage en cours")
# cadrillage
compt=0
#print(pas_x,pas_y)
while j < w :
    #print(j)
    #print(compt)
    ligne_vert(w-j)
    j += pas_x
    compt+=1

#print("fin horizontale")
compt=0
while i < h :
    #print(compt)
    if compt in passed_value:
        #print("in if")
        ligne_hor(h-i,"green")
    else:
        ligne_hor(h-i)
    i += pas_y
    compt +=1
#print("fin verticale")
# fin cadrillage

i,j=1,1

while j <= y:
    #print("j=",j)
    res=calc_three_nPlusOne(j)
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
