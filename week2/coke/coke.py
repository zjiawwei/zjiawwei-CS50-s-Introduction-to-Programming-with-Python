import sys
price = 50
total = 0
valid_coins = [25,10,5]
while total < 50:
    print(f"Amount Due:{price}")
    coin = int(input("Inter coin:"))
    if coin in valid_coins:
        price = price - coin
        total = total + coin
    else:
        print("Error")
        sys.exit()
change = total - 50
print(f"Change Owed:{change}")

