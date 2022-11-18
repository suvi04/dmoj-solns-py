i=int(input())
while True:
    a,b=input().split()   
    if int(a)>10 or int(b)>10:
        break
    print(int(a)+int(b))
    i-=1
    if i==0:
        break