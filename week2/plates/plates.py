def main():
    plate = input("Plate:")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    
def is_valid(s):
    return(is_len(s) and
           is_start_with_two_letter(s) and
           is_no_punctuation(s) and
           is_numbers_rules(s))
    
def is_len(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def is_start_with_two_letter(s):
    return s[0:2].isalpha()

def is_no_punctuation(s):
    for char in s:
        if not char.isalnum():
            return False
    return True
        
def is_numbers_rules(s):
    has_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not has_number:
                if char == '0':
                    return False
            has_number = True
        elif has_number:
            return False
    return True
main()