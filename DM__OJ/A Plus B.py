i=int(input())
while True:
    a,b=input().split()
    c=int(a)+int(b)
    print(c)
    i-=1
    if i==0:
        break