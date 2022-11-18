weight=float(input())
height=float(input())
bmi=weight/(height*height)
if bmi>25:
    print("Overweight")
if bmi<18.5:
    print("Underweight")
if bmi<=25 and bmi>=18.5:
    print("Normal weight")
