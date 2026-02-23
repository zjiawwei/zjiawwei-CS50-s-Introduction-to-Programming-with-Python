grocery = {}
while True:
    try:
        item = input().strip().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        print("\n")
        for item, count in sorted(grocery.items()):
            print(count, item, sep= " ")
        break