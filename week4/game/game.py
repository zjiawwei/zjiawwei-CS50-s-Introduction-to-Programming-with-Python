import random

while True:
    try:
        level = int(input("Level:"))
        if level > 0:
            break
    except ValueError:
        pass

while True:
    try:
        level = int(input("Guess:"))
        if level <= 0:
            continue
        if level < random.randint(1,level):
            print("Too small!")
        elif level > random.randint(1,level):
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass