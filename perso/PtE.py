class Env:
    lvl=None
    env_env=None
    objects=[]
    nb_env=0
    nb_obj=0
    def __init__(self,obj_env=None):  #args*
        print('Env_init')

        self.id_env=self.nb_env
        print("id env :",self.id_env)

        self.obj_env=obj_env
        if self.obj_env==None:
            print("no object")
        else :
            print("OBJ!")


class Obj:
    nb_obj=0
    def __init__(self,env_obj=None):
        print('objet __init__')

        self.id_obj=self.nb_obj

        self.env_obj=env_obj
        if self.env_obj==None:
            print("no env")
        else :
            print("env!")
            Env.nb_obj+=1
        print("id objet : ",self.id_obj)
        print("env objet :",self.env_obj)

        #super().__init__()


class Create_Env:
    def __init__(self,nom_env,x):
        self.x=x
        self.nom_env=Env()
        for i in range(self.x):
            nom_obj="objet"+str(self.x)
            self.nom_obj=Obj(self.nom_env)
            self.nom_env.objects += [self.nom_obj]
        print("objet de ",self.nom_env,"(env):",self.nom_env.objects)

    #### class Create def env; def obj ;def lv


print(" ######################################################")
print("Instruction: OBJ()   (objet sans env)")
print(" ######################################################")
objet1=Obj()
print(" ######################################################")
print("Instruction: Affichage de Valeur")
print("objet1",objet1)
print(" ######################################################")

print("Instruction: ENV(OBJ)  (obj1:instruction percedente)")
print(" ######################################################")
env1=Env(objet1)
print(" ######################################################")

print("Instruction: ENV()) (env sans objet")
print(" ######################################################")
env2=Env()
print(" ######################################################")
print("Instruction Affichage de Valeur")
print(" ######################################################")
print("id env1:",env2.id_env)
print(" ######################################################")

print(" Instruction: OBJ(ENV) (env1:instruction precedente)")
print(" ######################################################")
objet2=Obj(env2)
print(" ######################################################")
print("Instruction Affichage de Valeur")
print(" ######################################################")
print(" obj 2:",objet2.env_obj)
print("id obj 2:",objet2.id_obj)
print(" ######################################################")

try1=Create_Env("try1",5)
print(try1)
