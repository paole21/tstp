
import csv

with open("st.csv", "r", encoding="utf-8", newline= "") as f:
    r = csv.reader(f, delimiter= ",")
    for row in r:
        print(",".join(row))

