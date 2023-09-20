#Pyhtonにて記述

import math
count = 0

def div_eight(num):
    global count
    
    answer = num * 0.8
    answer = math.floor(answer)
    
    count += 1
    
    if count == 45:
        print(answer)
        return

    div_eight(answer)

div_eight(387420489)