List=[30,20,10]
print("현재리스트:",List)

print("10의 값의 위치:",List.index(10))

List.insert(2,200)
print("insert(2,200)후의 리스트:",List)

List.remove(200)
print("remove(200)후의 리스트:",List)

List.extend([555,666,555])
print("extend[555,666,555]후의 리스트:",List)

print("555값의 개수:",List.count(555))
