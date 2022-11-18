cal=0

a=int(input())
b=int(input())
c=int(input())
d=int(input())

if a==1:
    cal+=461
if a==2:
    cal+=431
if a==3:
    cal+=420
if a>=4:
    cal+=0

if b==1:
    cal+=100
if b==2:
    cal+=57
if b==3:
    cal+=70
if b>=4:
    cal+=0

if c==1:
    cal+=130
if c==2:
    cal+=160
if c==3:
    cal+=118
if c>=4:
    cal+=0

if d==1:
    cal+=167
if d==2:
    cal+=266
if d==3:
    cal+=75
if d>=4:
    cal+=0
print("Your total Calorie count is "+str(cal)+".")