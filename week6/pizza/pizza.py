import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith (".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1],newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
except FileNotFoundError:
    sys.exit("File does not exitst")

if not rows:
    sys.exit("Empty CSV file")
print(tabulate(rows[1:],headers=rows[0],tablefmt="grid"))