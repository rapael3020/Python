List=[30,20,10]
print("현재리스트:",List)

List.append(40)
print("append(40)후의 리스트:",List)

print("pop()으로 추출한 값: ",List.pop())
print("pop() 후의 리스트:",List)

List.sort()
print("sort() 후의 리스트:",List)

List.reverse()
print("reversed() 후의 리스트: ",List)
del(List[2])
print("del()후의 리스트:",List)

