def count_sev(num):
    count = 0

    for i in range(7, num+1, 7):
        string = str(i)
        count += string.count("7")
    
    print("{}までの7の倍数の内、\"7\"が含まれる回数は{}回です。".format(num, count))

count_sev(7777777)
