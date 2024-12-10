xmax=52 #origine+cg+d
xmin=0  #origine+cd-d
ymin=24
ymax=48
zmin=10
zmax=18
xmoy=26
ymoy=36
zmoy=14
taillex_env=400
tailley_env=500
taillez_env=20

import tkinter



pos=[[xmin,xmax],[ymin,ymax],[zmin,zmax]]
pos_env=[[0,taillex_env],[0,tailley_env],[0,taillez_env]]
pos_cg=[pos[0][1]-pos[0][0],pos[1][1]-pos[1][0],pos[2][1]-pos[2][0]]
pos_moy=[xmoy,ymoy,zmoy]
xmin+=2
pos=pos

class obj_3d:
    def __init__(self,pos):

        self.pos_xmin=pos[0][0]      #def par l'interval ?!
        self.pos_xmax=pos[0][1]
        self.pos_ymin=pos[1][0]
        self.pos_ymax=pos[1][1]
        self.pos_zmin=pos[2][1]
        self.pos_zmax=pos[2][1]
        self.pos=pos=[[self.pos_xmin,self.pos_xmax],[self.pos_ymin,self.pos_ymax],[self.pos_zmin,self.pos_zmax]]

        print(pos)

class vue_obj_3d:
    def __init__(self,pos):
        self.pos=pos
        #print(super())
        #self.master=super()
        self.tk=tkinter.Tk()
        self.frame=tkinter.Frame(self.tk)
        self.canvas=tkinter.Canvas(self.frame,width=taillex_env,height=tailley_env,bg="black")
        self.creer_vue(self.pos,"white")
        #a retravailler !! (down)
    def creer_vue(self,pos,color,pdv=[0,0,0]):
        print(pos)

        x1=pos[0][0]-pdv[0]
        print("x1:",x1)
        y1=pos[1][0]-pdv[1]
        print("y1:",y1)
        x2=pos[0][1]-pdv[1]
        print("x2:",x2)
        y2=pos[1][1]-pdv[2]
        print("y2:",y2)
        self.canvas.create_rectangle(x1+1,y1+1,x2+1,y2+1,fill=color)
        #self.canvas.create_rectangle(100,150,150,300,fill="white")
        self.frame.pack()
        self.canvas.pack()
        self.tk.mainloop()

env1=obj_3d(pos_env)
objet1=obj_3d(pos)
"""
vue_env1=vue_obj_3d(env1,env1.pos)
vue_obj1=vue_obj_3d(objet1,objet1.pos)
"""
vue_env1=vue_obj_3d(env1.pos)
vue_obj1=vue_obj_3d(objet1.pos)
