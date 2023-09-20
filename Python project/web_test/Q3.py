#pythonにて記述

alpha_list = ["A","B","C","D","E","F","G",
              "J","K","Q","T","V","W","X","Y","Z"]

string_list = []

for i in alpha_list:
    for j in alpha_list:
        for h in alpha_list:
            for n in alpha_list:
                for v in alpha_list:

                    string = (i+j+h+n+v)
                    remove_list = ["B","C","D","F","G","J","K","Q",
                        "V","W","X","Y","Z"]

                    if string.count(remove_list) >= 2:
                        continue

                    if string[1] == "A":
                        continue

                    elif string[3] == "E":
                        continue

                    elif string[1] == "T":
                        continue

                    else:
                        string_list.append(string)

print(len(string_list))

                


