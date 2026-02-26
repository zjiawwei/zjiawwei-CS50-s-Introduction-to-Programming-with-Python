from twttr import shorten

def test_upper():
    assert shorten("HeLLo") == "HLL"
    assert shorten("AEIOU") == ""

def test_lower():
    assert shorten("hello") == "hll"
    assert shorten("aeiou") == ""

def test_novowels():
    assert shorten("tst_twttr") == "tst_twttr"
    assert shorten("bcdfg") == "bcdfg"
    assert shorten("12123") == "12123"