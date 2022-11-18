while True:
    month=int(input())
    if month>12 or month<1:
        break
    date=int(input())
    if date>31 or date<1:
        break
    if month<2:
        print("Before")
        break
    if month>2:
        print("After")
        break
    if month==2:
        if date>18:
            print("After")
            break
        if date<18:
            print("Before")
            break
        if date==18:
            print("Special")
            break