a=input("enter a sentence\n")
b=len(a)
count1=0
count2=0
for i in range (0,b):
    if a[i].isupper()==True:
        count1=count1+1
    elif a[i].islower()==True:
        count2=count2+1
    else:
        continue
print("upper case letters-",count1)
print("lower case letters-",count2)
