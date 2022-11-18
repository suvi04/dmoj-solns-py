votes=int(input())
a_b=input()
a=a_b.count("A")
b=a_b.count("B")
if a>b:
    print("A")
elif b>a:
    print("B")
elif b==a:
    print("Tie")