print ("##############################################################\n")
print("debut programme : PtEV2.py\n")

class Env:

    objects=[]
    id_next_env=0
    nb_obj=0
    def __init__(self,obj_env=None):  #args*
        self.obj_env=obj_env

        if self.obj_env!=None:
            self.objects+=[self.obj_env]
            Env.nb_obj += 1
            super().__init__()
            self.master=self.obj_env
            #print("env de : ",self.master)
        else :
            self.master=None
            #print("env de : ",self.master)

        print("\nobjects:",self.objects)
        self.id_env=Env.id_next_env
        print("\nenv id:",self.id_env)
        Env.id_next_env += 1


class Obj:
    id_next_obj=0

    def __init__(self,env_obj=None):
        self.env_obj=env_obj

        if self.env_obj!=None:
            super().__init__()
            self.master=self.env_obj
            Env.objects+=[self.env_obj]
            #print("\nenv:",self.master)
        else :

            self.master=None
            #print("\nenv:",self.master)

        self.id_obj=Obj.id_next_obj
        print("\nobjet id : ",self.id_obj)
        Obj.id_next_obj +=1

class PdV:
    def __init__(self,obj=None,env=None):
        self.obj=obj
        self.env=env

"""
print("\n")
f_x=((f1^A)+(f2^A))^A+((f3^!A)+(f4^!A))^!A
Obj()
print("##############################################################")
Env()
"""

obj_x=Obj()
print ("essai 1 ok !(obj sans env)\n")



env_a=Env()
print("essai 2 ok !(env_a sans objet)\n")


obj_y=Obj(env_a)
print(env_a.objects)
print("essai 3 ok (objet_y avec (env_a sans objet)!\n")

env_b=Env(obj_y)
print("essai 4 ok (env_b avec obj_y (qui a deja un env ???))!\n")


env_c=Env(obj_x)
print("essai 5 ok (env_c avec obj_x(sans env))!\n")


obj_z=Obj(env_a)
obj_w=Obj(env_a)

print ("essai 6 ok!(2objet(z,w) de plus dans env_a )\n")

obj_k=Obj(obj_x)
print ("essai 7 ok!(obj_k ,objet de obj_x)\n")

"""
class Application(tk.Frame):
    elements=[]
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.hi_there = tk.Button(self)
        """
