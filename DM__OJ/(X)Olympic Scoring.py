n,b,s,g=input().split()
n=int(n)
b=int(b)
s=int(s)
g=int(g)

scr=b+(s*3)+(g*5)
diff=n-scr
if int(diff/5)==0:
    print("1")
else:
    if diff%5!=0:
        print(int((diff//5)+1))
    else:
        print(int(diff//5))
