#pythonにて記述

#余りを変数Overで定義
over = 0

#AとBの組み合わせを2重ループにて再現
for i in range(1,2001):
    for j in range(1,2001):

        #組み合わせを検証し、変数にインクリメントする
        over += i % j
        
#余りの合算値を表示
print(over)