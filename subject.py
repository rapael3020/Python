name = input("이름을 입력하시오: ")
num = int(input("학번을 입력하시오: "))
a = int(input("수학점수를 입력하시오: "))
b = int(input("국어점수를 입력하시오: "))
c = int(input("영어점수를 입력하시오: "))

sum = a+b+c
avg = (a+b+c)/3

print("총 득점은 ",sum,"점이고, 평균은 ",avg,"점 입니다.")

if avg >= 90:
    print("A학점입니다.")
elif avg >= 80:
    print("B학점입니다.")
elif avg >= 70:
    print("C학점입니다.")
elif avg >= 60:
    print("D학점입니다.")
else:
    print("F학점입니다.")
