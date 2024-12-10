

def oui(x):
    x=int(x)
    #print("oui!")
    if  x == 1:
        return 1
    elif x== 0:
        return 0
    else :
        print("oui :x")
        return None

def non(x):
    #print("non!")
    x=int(x)
    if x == 1 :
        return 0
    elif x == 0 :
        return 1
    else :
        print("non!")
        return None

def et(x,y):
    x=int(x)
    y=int(y)
    #print('"et" en cours\n')
    if x == 1:
        if y == 1:
            #print("X=1,Y=1")
            return 1
        else :
            #print("X=1,Y=0")
            return 0
    else :
        if y == 0:
            #print("X=0,Y=0")
            return 1
        else:
            #print("X=0,Y=1")
            return 0

def ou(x,y):
    x=int(x)
    y=int(y)
    #print('"ou" en cours\n')
    if x == 1:
        #print("X=1")
        return 1
    else :
        #print("X=0")
        if y == 0:
            #print("et Y=0")
            return 0
        else:
            #print("et Y=1")
            return 1

def data(x):

    if len(str(x))>1 :
        #print("len(data) > 0")
        osef=[]
        for i in range(len(str(x))):
            osef+=data(i)
        bin_data=bin(int(osef[0]))

    if x is bool():
        bin_data = x
    else:
        bin_data=bin(x)
        bin_data=bin_data[2:]
    return bin_data

def compare(x,y,fct,fct2=oui):
    if len(x) == len(y):
        var=len(x)
        #print(var,"(base10) = ",bin(var),"(base2)" )
        var=str(bin(var)) #attention bin 4 != 100 !!!
        var=var[2:]
        var=int(var)
        result = [var]
        for i in range(len(y)):
            y_temp=y[i]
            x_temp=x[i]
            #print("x_temp(",i,") :",x_temp,", y_temp(",i,") :",y_temp,", fct :",fct)
            osef1=fct2(x_temp)
            osef2=fct2(y_temp)

            osef=fct(x_temp,y_temp)
            osef3=fct(osef1,osef2)
            #print("osefs|osef:",osef,",osef1 :",osef1,",osef2 :",osef2,",osef3 :",osef3)
            #print("osef =",osef,"; fct=",fct)
            result.append(osef)
            #result[1]+=str(osef)  !!!  reslult=[var,0]!!!
    else :
        print("not the same length")
        result=None
    return result

def affiche():
    seq_x="001111011111111"
    seq_y="100000001101100"
    print("longueur sequence:",len(seq_x))

    print("sequence_x:",seq_x)
    print("sequence_y:",seq_y)
    
    resultat=compare(seq_x,seq_y,ou)

    print("oui ou",resultat)


    resultat=compare(seq_x,seq_y,et)
    print("oui et",resultat)
    reslutat=compare(seq_x,seq_y,et,non)
    print("non et",resultat)

    seq_x="1101"

    resultat=compare(seq_x,seq_y,et)
    print(resultat)
    resultat=compare(seq_x,seq_y,ou)
    print(resultat)

    seq1=100
    seq4=255
    seq5=256
    seq2=0
    seq3=1

    print("sequence 1",data(seq1))
    print("sequence 2",data(seq2))
    print("sequence 3",data(seq3))
    print("sequence 4",data(seq4))
    print("sequence 5",data(seq5))

    print("\n")
    print(seq3,"et",seq2,":",et(seq3,seq2))
    print(seq2,"et",seq3,":",et(seq2,seq3))
    print(seq2,"et",seq2,":",et(seq2,seq2))
    print(seq3,"et",seq3,":",et(seq3,seq3),"\n")
    print("########################### \n")
    print(seq3,"ou",seq2,":",ou(seq3,seq2))
    print(seq2,"ou",seq3,":",ou(seq2,seq3))
    print(seq2,"ou",seq2,":",ou(seq2,seq2))
    print(seq3,"ou",seq3,":",ou(seq3,seq3))
    print("########################### \n")
    print(seq3,"non ou",seq2,":",non(ou(seq3,seq2)))
    print(seq2,"non ou",seq3,":",non(ou(seq2,seq3)))
    print(seq2,"non ou",seq2,":",non(ou(seq2,seq2)))
    print(seq3,"non ou",seq3,":",non(ou(seq3,seq3)))
    print("########################### \n")
    print(seq3,"non et",seq2,":",non(et(seq3,seq2)))
    print(seq2,"non et",seq3,":",non(et(seq2,seq3)))
    print(seq2,"non et",seq2,":",non(et(seq2,seq2)))
    print(seq3,"non et",seq3,":",non(et(seq3,seq3)))

    print("sequence 3 et non 2",et(seq3,non(seq2)))
    print("sequence non 3 et non 2",et(non(seq3),non(seq2)))
    print("sequence 2 et non 3",et(seq2,non(seq3)))

affiche()
