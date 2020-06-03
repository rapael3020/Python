i=1
flag=True
while flag:
    print(i,"종속문장",end='')
    if i == 10:
        flag = False
    i+=1

i=0
while True:
    if i == 3:
        break
        print("3출력")
    print(i,"출력")
    i+=1

print("다음문장")
