import sys
import os

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
elif not os.path.exists(sys.argv[1]):
    sys.exit("File does not exist")

try:
    line_count = 0
    with open(sys.argv[1]) as file:
        for line in file:
            line_strip = line.strip()
            if not line_strip:
                continue
            if line_strip.startswith('#'):
                continue
            line_count += 1
    print(line_strip)
except Exception as e:
    sys.exit(f"Error reading file{e}")
