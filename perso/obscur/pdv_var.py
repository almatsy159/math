import tkinter

main = tkinter.Tk()
frame = tkinter.Frame(main)

h_mini_map=200
w_mini_map=200
pdv_init = [100,200]
origine = 100,100
#cube_f1 = [100,100,300,300]
cube_f1 = [150,150,250,250]
#cube_f2=[]
cube_f6 = [150,150,250,250]


minimap = tkinter.Canvas(frame,height=h_mini_map,width=w_mini_map)
map = tkinter.Canvas(frame,height=h_mini_map*2,width=w_mini_map*2)
#minimap.create_rectangle()
map.create_rectangle(cube_f6[0],cube_f6[1],cube_f6[2],cube_f6[3],fill="green")
map.create_rectangle(cube_f1[0],cube_f1[1],cube_f1[2],cube_f1[3],fill="blue")
map.create_line(0,0,400,0)
map.create_line(0,400,400,400)
map.create_line(400,400,0,400)
minimap.create_line(0,400,0,0)
minimap.create_line(0,0,200,0)
minimap.create_line(0,200,200,200)
minimap.create_line(200,200,0,200)
minimap.create_line(0,200,0,0)
minimap.create_rectangle(cube_f1[0]/2,cube_f1[1]/2,cube_f1[2]/2,cube_f1[3]/2,fill="red")
minimap.create_rectangle(pdv_init[0]-1,pdv_init[1]-1,pdv_init[0]+1,pdv_init[1]+1,fill="black")
map.pack()
minimap.pack()
frame.pack()
main.mainloop()
