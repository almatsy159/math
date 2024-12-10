print ("##############################################################\n")
print("debut programme : PtEV2.py\n")

class Env:
    lvl=None
    env_env=None
    objects=[]
    nb_env_creer=0
    nb_obj=0

    def __init__(self,obj_env=None):  #args*
        print("env init")
        self.obj_env=obj_env
        self.id_env=self.nb_env_creer
        print("id env :",self.id_env)
        if self.obj_env!=None:
            print("OBJ! il y en a !")
            self.objects+=[self.obj_env]
            self.nb_obj+=1
            super().__init__()
            self.master=self.obj_env
            print("master:",self.master)
            self.master.nb_obj_creer+=1
        else :
            print("cet env n'as pas d' OBJ!")
            self.master=None
            print(self.master)
        print("objects:",self.objects)
        self.nb_env_creer+=1


class Obj:

    nb_obj_creer=0

    def __init__(self,env_obj=None):
        print("objet init")

        self.env_obj=env_obj
        self.id_obj = self.nb_obj_creer
        print("id objet:",self.id_obj)
        if self.env_obj!=None:
            print("Je suis un OBJ dans un ENV:")
            super().__init__()
            self.master=self.env_obj
            print(self.master)
        else :

            print("NO ENV")
        self.nb_obj_creer+=1
        print("nb obj creer:",self.nb_obj_creer)


print("0\n")
obj0=Obj()
print("1\n")
env_0=Env(obj0)
print("2\n")
obj1=Obj(env_0)
print("3\n")
obj2=Obj(env_0)
print("4\n")
"""set affichage 1:

obj_x=Obj()
print ("essai 1 ok !(obj sans env)\n")



env_a=Env()
print("essai 2 ok !(env_a sans objet)\n")


obj_y=Obj(env_a)
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
