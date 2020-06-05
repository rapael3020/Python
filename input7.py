kg1 = float(input("첫 번째 물건의 무게를 입력하시오: "))
kg2 = float(input("두 번째 물건의 무게를 입력하시오: "))
more = 600 - (kg1+kg2)

print("현재 엘리베이터의 허용무게는 {}kg 입니다.".format(more))
