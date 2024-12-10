class Env:
    lvl=None
    env_env=None
    objects=[]
    nb_env=0
    def __init__(self):  #args*
        print('Env_init')
        self.id_env=self.nb_env
        print("id env :",self.id_env)
        print("nb :",self.nb_env)
        self.nb_env+=1
        print("nb :",self.nb_env)


class Obj:
    nb_obj=0
    def __init__(self,env_obj=None):
        self.id_obj=self.nb_obj
        self.env_obj=env_obj
        print('objet __init__')
        print("id objet : ",self.id_obj,";env objet :",self.env_obj)

        #super().__init__()
        """
class lvl:
    def __init__(self,obj):
        if obj.env_obj==None:
            self.lvl=0
            print("lvl =0")
        else :
            self.lvl+=1
            print("lvl = ",self.lvl)
            """
class sing:
          lvl=None
          def __init__(self,obj):
              print("is sys ?")
              if obj.env_obj==None:
                  self.lvl=0
                  sys_init=True
                  print("yes")
              else :
                  print("no")
                  self.lvl+=1
                  sys_init=False


class lvl_sing(sing):
        lvl=None
        def __init__(self):
            super().__init()




objet1=Obj()
env1=Env()
objet2=Obj(env1)
print(objet2)
print("lvl objet1 : ",lvl_sing())
print("lvl objet2 : ",lvl_sing())
#print("lvl objet2 (V2) :",objet2.lvl)
"""
Parent("john")
Enfant()
"""



#Enfant(Parent())
