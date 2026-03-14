from validator_collection import validators,errors

def main():
    print(validate(input("What'd your email address?").strip()))

def validate(s):
    try:
        validators.email(s)
        return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"

if __name__ == "__main__":
    main()