def main():
    user_input = input("Input:")
    result = shorten(user_input)
    print(f"Output:{result}")
    
def shorten(world):
    result = ""
    vowels = "AEIOUaeiou"
    for char in world:
        if char not in vowels:
            result = result + char
    return result

if __name__ == "__main__":
    main()