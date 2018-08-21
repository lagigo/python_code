score = float(input("輸入分數:"))


if 90<=score<=100 :
    print ("A級")
elif 80<=score<90 :
    print ("B級")
elif 70<=score<80 :
    print ("C級")
elif 60<=score<70 :
    print ("D級")
elif 50<=score<60 :
    print ("你是不是智障")
elif 0<=score<50 :
    print ("拉基")
if score<0 or score>100 :
    print ("你為什麼連分數都輸入錯")
