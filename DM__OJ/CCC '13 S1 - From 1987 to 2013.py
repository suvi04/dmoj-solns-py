year=input()

year=int(year)
while True:
    one=year.count(1)
    two=year.count(2)
    three=year.count(3)
    four=year.count(4)
    five=year.count(5)
    six=year.count(6)
    seven=year.count(7)
    eight=year.count(8)
    nine=year.count(9)
    zero=year.count(0)
    if one>1 or two>1 or three>1 or four>1 or five>1 or six>1 or seven>1 or eight>1 or nine>1 or zero>1:
        print(year)
    
    year+=1