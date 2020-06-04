ls=[0,0,0,0]; Sum=0

print("len(ls):",len(ls))
for i in range(len(ls)):
    ls[i]=int(input(str(i)+"째 숫자 입력: "))
    Sum+=ls[i]

for i in range(len(ls)):
    print("ls[%d]:%d"%(i,ls[i]))
print("리스트의 합:%d"%Sum)
