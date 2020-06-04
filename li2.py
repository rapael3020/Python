ls = [10,20,30,40]
arr=ls #얕은복사 ->깊은복사도 알아보기

print("ls: ",ls)

print("\nls[1:3]=>ls[1]~ls[2]:",ls[1:3])
print("ls[0:3]=>ls[0]~ls[2]:",ls[0:3])
print("ls[2:]=>ls[2]~끝까지:",ls[2:])
print("ls[:2]=>ls[0]~ls[2]:",ls[:2])


print("ls:{}ls,id:{}".format(ls,id(ls)))
print("arr:{}arr,id:{}".format(arr,id(arr)))
      
