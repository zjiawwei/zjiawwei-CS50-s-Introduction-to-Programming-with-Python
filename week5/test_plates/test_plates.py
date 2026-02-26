from plate import is_valid

def test_long():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    
def test_number():
    assert is_valid("AB012") == False
    assert is_valid("AB12C") == False
    assert is_valid("ABC12") == True

def test_null():
    assert is_valid("AB!23") == False
    assert is_valid("ab12") == True

def test_lower():
    assert is_valid("abc12") == True
    assert is_valid("CS50") == True