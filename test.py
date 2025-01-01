import pytest
from main import count_vowels

def test_count_vowels_all_vowels():
    # Строка, содержащая только гласные
    assert count_vowels("aeiouAEIOU") == 10

def test_count_vowels_no_vowels():
    # Строка, не содержащая гласных
    assert count_vowels("bcdfghjklmnpqrtvwxz") == 0

def test_count_vowels_mixed_case():
    # Строка, содержащая как прописные, так и строчные гласные
    assert count_vowels("Hello World") == 3

def test_count_vowels_empty():
    # Пустая строка
    assert count_vowels("") == 0

@pytest.mark.parametrize("s, expected", [
    ("aeiou", 5),          # только гласные
    ("aeioudfjkls", 5),    # смешанная строка
    ("rhythm", 0),         # строка без гласных
    ("aA", 2),             # строка с прописными и строчными буквами
    ("", 0)                # пустая строка
])
def test_count_vowels_parametrized(s, expected):
    assert count_vowels(s) == expected
