from response import validate

def test_valid_email():
    assert validate("zjiawwei@gmail.com") == "Valid"
    assert validate("malan@harvard.edu") == "Valid"

def test_invalid_email():
    assert validate("malan@@@harvard.edu") == "Invalid"
    assert validate("zjiawwei@@@gmail.com") == "Invalid"
    assert validate("zjiwwei@gmail..com") == "Invalid"