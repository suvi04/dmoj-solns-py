i=int(input())
t=0
T=0
s=0
S=0
while i>0:
    abc=input()
    t+=abc.count("t")
    T+=abc.count("T")
    s+=abc.count("s")
    S+=abc.count("S")
    i-=1


if (t+T)>(s+S):
    print("English")
if (T+t)<(s+S):
    print("French")
if (t+T)==(s+S):
    print("French")
    