def can_div_three(para, para_2):
    if para % 3 == 0:
        print(str(para) + "は、3で割り切れるよ…")
    
    else:
        print(str(para) + "は、3じゃ割り切れないよ")

    if para == para_2:
        return
    
    para += 1
    
    can_div_three(para, para_2)

can_div_three(1, 50)