import pytest

from lib.palindrome import longest_palindromic_substring as palindrome


@pytest.fixture
def result():
    return palindrome("racecar")


@pytest.mark.parametrize("bad", [None, 2, 3.14, [], {}, (), set()])
def test_rejects_non_string_types(bad):
    with pytest.raises(TypeError):
        palindrome(bad)


def test_palindrome_length():  # length should not excceed 100
    input_str = "a" * 101
    with pytest.raises(ValueError):
        palindrome(input_str)


def test_palindrome_content(result):
    assert palindrome(result).isalnum()  # only alphanumeric characters
    with pytest.raises(ValueError):
        palindrome("A man with long hair")


def test_palindrome_longest():
    out = palindrome("abc")  # only singles
    assert isinstance(out, str)
    assert len(out) == 1
    assert out in set("abc")
    assert palindrome("abaxyzzyxf") == "xyzzyx"


def test_rejects_empty_and_blank():
    with pytest.raises(ValueError):
        palindrome("")
    with pytest.raises(ValueError):
        palindrome("   ")
