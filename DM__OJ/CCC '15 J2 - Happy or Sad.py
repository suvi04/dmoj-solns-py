abc=input()
h=abc.count(":-)")
s=abc.count(":-(")

if h>s:
    print("happy")
elif h<s:
    print("sad")
elif h==s and h!=0:
    print("unsure")
else:
    print("none")