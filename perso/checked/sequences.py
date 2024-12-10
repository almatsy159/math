natif_poss_2bit=["00","01","10","11"]
generated_poss_2bit=[]
generated_poss_4bit=[]
natif_poss_1bit=["0","1"]

# look like a full join fct
def generate(poss,A=1):
    generated=[]
    for i in range(len(poss)):
        """
        if A:
            osef=pow(len(poss),2)
        else:
            osef=pow(len(poss),2) - len(poss)
        """
        for j in range(len(poss)):

            generated.append(str(poss[i])+str(poss[j]))

    return generated

generated_poss_2bit=generate(natif_poss_1bit)
print(generated_poss_2bit)
generated_poss_4bit=generate(natif_poss_2bit)
print(generated_poss_4bit)

# 
def compare(seqA,seqB=""):
    result=[]
    if seqB == "":
        for i in range(len(seqA)):
            seqB+=("0")
    if len(seqA) > len(seqB):
        size=len(seqB)
        reste=str(seqA[len(seqB):])
    elif len(seqA) < len(seqB):
        size=len(seqA)
        reste=str(seqB[len(seqA):])
    else:
        size=len(seqA)
        reste=""

    for i in range(size):
        if seqA[i]==seqB[i]:
            if seqA[i]==1:
                result.append("A=1==B")
            else:
                result.append("A=0==B")

        else:
            if seqA[i]==1:
                result.append("A=1!=B")
            else:
                result.append("A=0!=B")
        if reste != "":
            result.append(reste)
    return result

"""

for i in range(size):
    result.append("A=")
    if seqA[i]==1:
        result.append("1")
        if seqA[i]==seqB[i]:
            result.append("==B")
        else:
            result.append("=!B")

    else:
        result.append("0")
        if seqA[i]==seqB[i]:
            result.append("==")
        else:
            result.append("!=")
    result.append("B")
if reste != "":
    result.append(reste)
return result
"""





seqA="1100"
seqB="1010"

result=compare(seqA,seqB)
print("seqA :",seqA,"\nseqB :",seqB)
for i in range(len(seqA)):
    print("\nseqA[",i,"] :",seqA[i],"\nseqB[",i,"] :",seqB[i],"=> result :",result[i])

"""
def exec_result(x):
    part1=x[0:2]
    part2=x[3:4]
    part3=x[5]
    exec(part1)
    if part2 == "==":
        part3=A
    else:
        part3=!A
"""
