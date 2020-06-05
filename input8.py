high = int(input("키를 입력하세요: "))
kg = float(input("현재 몸무게를 입력하시오: "))
avg = ((high - 100)*0.9)
fat = (kg/avg)*100

print("표준체중은 ",avg,"kg이고, 비만도는 ",fat,"% 입니다.")
