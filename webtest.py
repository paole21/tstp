
def train_fare(age):
    """引数ageが12以上の時は10000を、6以上12未満の場合は5000、
    6未満の場合は0を返す、運賃を求める関数です。
    """

    if age >=6 and age < 12:
        print(5000)

    elif age < 6:
        print(0)

    else:
        print(10000)

