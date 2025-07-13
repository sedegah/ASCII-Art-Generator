from ascii_generator.convert import get_ascii_char, CHARSETS

def test_ascii_mapping():
    dense = CHARSETS['dense']
    assert get_ascii_char(0, dense) == dense[0]
    assert get_ascii_char(255, dense) == dense[-1]

def test_charset_selection():
    for key in CHARSETS:
        assert isinstance(CHARSETS[key], str)
        assert len(CHARSETS[key]) > 0
