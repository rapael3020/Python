num,result,i=0,0,1
while True:
    num = int(input("10~20사이 숫자 입력:"))
    if num<10 or num>20:
        print("잘못입력")
        continue
    break
else:
    print("next,,,")
while i <=num:
    result+=i
    i+=1
else:
    print("1~",num,"까지의 합: ",result)
