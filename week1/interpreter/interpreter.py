str_input = input("Expression:").strip()
x, y, z = str_input.split(" ")

num1 = float(x)
num2 = float(z)

match y:
    case '+':
        print(f"{num1 + num2:.1f}")
    case '-':
        print(f"{num1 - num2:.1f}")
    case '*':
        print(f"{num1 * num2:.1f}")
    case '/':
        if num2 == 0:
            print("ERROR")
        else:
            print(f"{num1/num2:.1f}")