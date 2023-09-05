if __name__ == "__main__":
    
    import csv

    my_list = []

    def guess():
        print("answer question or quit to type q")
        while True:
            try:
                ans = input("What animals do you like ?")
                ans = str(ans)
                if ans == "q":
                    break
                else:
                    my_list.append(ans)

            except:
                print("何らかのエラーが発生しました。")

    guess()

    with open("challenge2.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=",")
        w.writerow(my_list)

        
