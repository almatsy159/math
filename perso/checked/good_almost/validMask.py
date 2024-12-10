x=input(" mask : ")
y=input(" ip : ")



def is_bin_mask(x):
    err = 1
    flag=0
    if len(x) == 32:
        for i in range(len(x)):
            if x[i] == "0":
                flag=1
                if i == 0:
                    err = 6
                    print("invalid mask error",err," mask should start by 1")
                    return err
            else :
                if flag==1:
                    err=4
                    print("invalid mask error",err," mask not conform")
                    return err
    else:
        if len(x)<32:
            err = 3
            print("invalid mask error",err," mask too short; length = ",len(x))
        else:
            err=2
            print("invalid mask error",err," mask too long; length = ",len(x))
        return err
    if err == 1 and flag == 1:
        return True
    else:
        if flag == 0:
            err =5
            print("invalid mask error",err," mask is too big")
        return err

flag_bin = 1
for i in x:
    #print("binary = ",binary)
    if (i !='1' and i != '0') and flag_bin == 1:
        print(type(i))
        flag_bin = 0
        print("mask not binary")


if flag_bin ==1:
    z=is_bin_mask(x)
    print(z)
"""
elif int(x):
    z= is_dec_mask(x)
elif hex(x):
    z = is_hex_mask(x)
else print("unreadable mask")
"""
