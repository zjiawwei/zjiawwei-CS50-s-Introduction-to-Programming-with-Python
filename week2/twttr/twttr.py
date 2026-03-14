text = input("Input:")

result = ""
vowels = "AEIOUaeiou"

for char in text:
    if char not in vowels:
        result = result + char

print(f"Output:{result}")