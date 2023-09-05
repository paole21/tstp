import re

def train_fare(age):
    """引数ageが12以上の時は10000を、6以上12未満の時5000を、
    6未満の時は0を返す、運賃を出力する関数です。
    """

    age = re.findall("\d", age, re.IGNORECASE)
    age = int(age[0])
        
    if age >= 12:
        print(10000)

    elif age >= 6 and age <12:
        print(5000)

    elif age < 6 and age >= 0:
        print(0)

    elif age < 0:
        print("正の整数を入力してください")


train_fare(3)
train_fare(9)
train_fare(34)
train_fare(-8)
train_fare("三十七")
