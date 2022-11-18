limit=float(input())
act_speed=float(input())
if act_speed<=limit:
    print("Congratulations, you are within the speed limit!")
diff=act_speed-limit
if act_speed>limit:
    if diff<=20 and diff>=1:
        fine=100
    if diff<=30 and diff>=21:
        fine=270
    if diff>=31:
        fine=500

    print("You are speeding and your fine is $"+str(fine)+".")