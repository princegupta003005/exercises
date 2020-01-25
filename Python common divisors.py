a=int(input())
b=int(input())
while (b%a>0):
    temp=b%a
    b=a
    a=temp
print(a)