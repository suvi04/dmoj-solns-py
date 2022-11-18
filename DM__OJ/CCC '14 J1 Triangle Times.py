while True:
    a1=int(input())
    if a1<0 or a1>180:
        break
    a2=int(input())
    if a2<0 or a2>180:
        break
    a3=int(input())
    if a3<0 or a3>180:
        break
    if a1+a2+a3==180:
        if a1==a2==a3==60:
            print("Equilateral")
            break
        if a1!=a2 and a2!=a3 and a1!=a3:
            print("Scalene")
            break
        if a1==a2 or a2==a3 or a3==a1:
            print("Isosceles")
            break


    else:
        print("Error")
        break