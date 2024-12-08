turple1=(1,2,3,2,1)



def palidrome(turple1):
    s=0
    end=len(turple1) -1
    while s < end:
        if turple1[s]!=turple1[end]:
            return False
        s+=1
        end-=1
    return True
flag=palidrome(turple1)
if flag:
    print("palidrome")
else:
    print("not palidrome")