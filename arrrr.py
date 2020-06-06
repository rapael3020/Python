ls=[10,20,30]
arr=[40,50,60]

print("ls:",ls)
print("arr:",arr)

Str=ls+arr
print("ls+arr=>Str:",Str)

string =ls*3
print("ls*3=>string:",string)

Str=[0,0,0]
for i in range(len(Str)):
    Str[i] = ls[i]+arr[i]

print("ls+arr=>Str:",Str)
string=[0,0,0]
for i in range(len(string)):
    string[i]=ls[i]*3

print("ls*3=>string",string)
