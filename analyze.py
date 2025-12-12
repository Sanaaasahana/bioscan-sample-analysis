import csv
rows = [["id","value"], [1, 3.14], [2, 2.71]]
with open("output.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print("Analysis complete — output.csv written")
