a=int(input())
b=int(input())
c=int(input())
if a>b>c:
    print(b)
if a>c>b:
    print(c)
if b>c>a:
    print(c)
if b>a>c:
    print(a)
if c>a>b:
    print(a)
if c>b>a:
    print(b)