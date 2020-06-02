i,j,sum=0,1,0
for i in range (1,1001):
    while j<i:
        if i%j == 0:
            sum+=j
        j+=1
    j=1
    if i ==sum:
        print(i)
    sum=0
