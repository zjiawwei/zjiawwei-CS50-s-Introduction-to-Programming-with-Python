name_input = input("camelCase:").strip()
snake_name = ""
for char in name_input:
    if char.isupper():
        snake_name = snake_name + "_" + char.lower()
    else:
        snake_name = snake_name + char
print("snake_case:",snake_name)