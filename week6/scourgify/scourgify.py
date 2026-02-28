import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")


try:
    with open(sys.argv[1], newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        students = []
        for row in reader:
            last,first = row['name'].split(',')
            students.append({
                'first':first,
                'last':last,
                'house':row['house']
            })
            print(row['name'],row['house'])
    with open(sys.argv[2],"w",newline='') as csvfile:
        fieldnames = ['first','last','house']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")