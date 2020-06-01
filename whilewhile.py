for i in range(0,3,1):
    for k in range(0,5,1):
        if k ==3:
            break
        print("(i:%d\tk:%d)"%(i,k))
        
i=0
while i<3:
    k=0
    while k<5:
        if k ==3:
            break
        print("(i:%d\tk:%d)"%(i,k))
        k+=1
    i+=1
