a={'nitin':9,'aython':2,'cat':7}
def sortee():
    b=sorted(a.items(),key= lambda t:t[0])
    print(b)
sortee()
def sumog():

    q=sum(a.values())
    print(q)
sumog()
def reverse():
    g={y:x for x,y in a.items()}
    print(g)
reverse()