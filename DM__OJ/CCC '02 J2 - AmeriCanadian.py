while True:
    txt=input()
    if txt=="quit!":
        break
    if len(txt)>4 and txt.endswith("or"):
        txt1=txt.replace("aor","aour").replace("bor","bour").replace("cor","cour").replace("dor","dour").replace("for","four").replace("gor","gour").replace("hor","hour").replace("jor","jour").replace("kor","kour").replace("lor","lour").replace("mor","mour").replace("nor","nour").replace("por","pour").replace("qor","qour").replace("ror","rour").replace("sor","sour").replace("tor","tour").replace("vor","vour").replace("wor","wour").replace("xor","xour").replace("zor","zour")
        print(txt1)
    else:
        print(txt)
