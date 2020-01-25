a=int(input())
flag=0
if a==1:
    print("not a prime number")
else:
    for i in range (2,a):
        if a%i==0:
            flag=1
if flag==0:
    print("IT IS PRIME NUMBER")
else:
    print("NOT A PRIME NUMBER")
