
import csv

with open("村田さん改善＿1コース表.csv", "r", encoding="utf-8", newline="") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
    
