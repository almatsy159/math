class system():
    id=0
    def __init__(self,name,*args):
        self.items=[]
        for i in args:
            self.items.append(i)
        self.name=name
        self.id=system.id
        system.id+=1

    def fct_transfert(self,fct,*args):
        print(args)
        print(args[0],args[1])
        x=[]
        for i in range(len(args)):
            x.append(i)
        """
        for j in range(len(x)):
            osef="args["+str(x[j])+"]"
            y=osef
        """
        #object(osef)
        print(x)
        self.result=fct(args[0],args[1])



def fonction1(k,x):
    result = k*x
    return result
x=10
y=10
z=5
size={"x":x,"y":y,"z":z}
comp=["obj1","obj2","etc..."]
law="3x+1"
data=[10]
color="green"
sys1=system("test",{1:size,2:comp,3:law,4:data},color)

print("Sys1 :\n Items:",sys1.items,"\n Id :",sys1.id)
print(sys1.items[0][1]["x"])
sys1.fct_transfert(fonction1,3,sys1.items[0][1]["x"])
print(sys1.result)
