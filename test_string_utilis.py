import pytest
from string_utils import StringUtils


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, result",
    [
        ("Привет", "Привет"),
        (
            "нельзя просто так взять и написать код без слез.",
            "Нельзя просто так взять и написать код без слез.",
        ),
    ],
)
def test_positive_text(input_text, result):
    text = StringUtils()
    assert text.capitalize(input_text) == result


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, result",
    [
        ("", ""),
        (" ", " "),
        ("ТЕХНИКИ тест-дизайна", "ТЕХНИКИ тест-дизайна"),
        ("123skypro", "123skypro"),
    ],
)
def test_negative_text(input_text, result):
    text = StringUtils()
    assert text.capitalize(input_text) == result


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, result",
    [
        ("   skypro", "skypro"),
        ("Hello", "Hello"),
        (" sky ", "sky "),
        ("Hello world", "Hello world"),
        ("Привет", "Привет"),
    ],
)
def test_positive_trim(input_text, result):
    text = StringUtils()
    assert text.trim(input_text) == result


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, result", [("   ", ""), ("", ""), ("\n Катя", "\n Катя")]
)
def test_negative_trim(input_text, result):
    text = StringUtils()
    assert text.trim(input_text) == result


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, symbol, result",
    [
        ("skypro", "y", True),
        ("Привет", "е", True),
        (" sky ", "p", False),
        ("Hello world", " ", True),
        (" ", " ", True),
        ("Как дела?", "?", True),
        ("User125", "2", True),
    ],
)
def test_positive_contains(input_text, symbol, result):
    text = StringUtils()
    assert text.contains(input_text, symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, symbol, result",
    [
        (" sky ", "p", False),
        (" ", " ", True),
        ("Hello", "h", False),
        ("World", "о", False),
    ],
)
def test_negative_contains(input_text, symbol, result):
    text = StringUtils()
    assert text.contains(input_text, symbol) == result


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, symbol, result",
    [
        ("skypro", "y", "skpro"),
        ("Привет", "е", "Привт"),
        ("Hello world", " ", "Helloworld"),
        ("Skypro", "", "Skypro"),
        ("Казнить нельзя, помиловать", ",", "Казнить нельзя помиловать"),
        ("Skypro", "Pro", "Skypro"),
        ("Привет, мир", ", мир", "Привет"),
        ("Skypro", "Skypro", ""),
    ],
)
def test_positive_delete_symbol(input_text, symbol, result):
    text = StringUtils()
    assert text.delete_symbol(input_text, symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, symbol, result", [("sky", "p", "sky"), ("", "", "")]
)
def test_negative_delete_symbol(input_text, symbol, result):
    text = StringUtils()
    assert text.delete_symbol(input_text, symbol) == result
