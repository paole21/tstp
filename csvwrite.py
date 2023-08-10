
import csv

with open("st.csv", "w") as f:
          w = csv.writer(f, delimiter= ",")
          w.writerow(["red", "green", "blue"])
          w.writerow(["purple","black", "white"])
