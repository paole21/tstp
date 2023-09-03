def right_down(times):
    times = int(times)

    for i in range(0, times):
        if i == 0:
            print("■")

        elif i == times:
            break
        
        else:
            indent = " "
            print(indent * i + "■")


times = input("表示したい段数を入力してください。")
right_down(times)



def right_down_sub(times):
    times = int(times)

    for i in range(1,times +1):
        for j in range(1,times +1):
            
            if i == j:
                print(" " * (j-1) +"■")
                break
            
            else:
                continue
    
    return

right_down_sub(times)