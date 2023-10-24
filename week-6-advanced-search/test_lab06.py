import pytest
from lab06_advanced_search import advanced_search

def test_advanced_search(user_file, search_word):
    assert advanced_search('"Lab06.empty.json"', "Empty") == "Term was not found."
    assert advanced_search("Lab06.trivial.json", "trivial") == "Term was found."
    assert advanced_search("Lab06.trivial.json", "missing") == "Term was not found."
    assert advanced_search("Lab06.languages.json", "C++") == "Term was found."
    assert advanced_search("Lab06.Languages.json", "Lisp") == "Term was not found."
    assert advanced_search("Lab06.countries.json", "United States of America") == "Term was found."
    assert advanced_search("Lab06.countries.json", "United States") == "Term was not found."