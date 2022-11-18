a=int(input())
a_list=[]
while True:
    if a%2==0:
        a_list.append(1)
    if a%3==0:
        a_list.append(a)
    if a%5==0:
        a_list.append(a)
    if a%7==0:
        a_list.append(a)
    if a%11==0:
        a_list.append(a)
    if a%13==0:
        a_list.append(a)
    if a%17==0:
        a_list.append(a)
    if a%19==0:
        a_list.append(a)
    if a%23==0:
        a_list.append(a)
    if a%29==0:
        a_list.append(a)
    if a%31==0:
        a_list.append(a)
    break
print(len(a_list))