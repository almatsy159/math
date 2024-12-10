base=10
val=10
puissance=10
"""
var="hi"
dico={"hi":"val1","hey":"val2"}
print("{hey}".format(**dico))
print(f"xxx {var} xxx)")
x=pow(val,puissance)
text="="
print("{:>10}\n{:>8}{:>4}{:>15}\n{:>10}".format(puissance,val,text,x,base))
"""
def base(x,base_init=2,base_finale=10):
    print("#####################################################################")
    x=str(x)
    tab1=[]
    tmp=0
    chaine=""
    resultat=0
    for i in range(len(x)):
        tab1.append(x[i])
    print("tab1:",tab1,"\n")
    tab2=[]
    for i in range(len(tab1)):
        #tmp = base_init^î
        print("i:",i,";base:",base_finale)
        tmp=pow(base_finale,i)
        print("tmp=base_finale^i:",tmp)
        x1=tab1[len(tab1)-(i+1)]
        x1=int(x1)
        chaine=str(base_init)+"^"+str(i)
        print("chaine:",chaine,"= temp:",tmp)

        tab2.append(tmp*x1)
        print("\n")
    print("tab2:",tab2)
    for i in tab2:
        resultat+=i
    return resultat
#print(base(101))
print(base(12,10,2))
#print(base(124,10,10))
#print(base(100001))
