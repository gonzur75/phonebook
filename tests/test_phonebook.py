import pytest


def test_lookup_by_name(phonebook):
    phonebook.add("John", "1234")
    assert phonebook.lookup("John") == "1234"


def test_phonebook_contains_specific_name(phonebook):
    phonebook.add("John", "1234")
    assert "John" in phonebook.names()


def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError) as excinfo:   #
        phonebook.lookup("Monika")

    assert "Monika" in str(excinfo.value)


def test_empty_phonebook_is_consistent(phonebook):
    assert phonebook.is_consistent()


def test_is_consistent_with_different_entries(phonebook):
    phonebook.add('Monika', "0800")
    phonebook.add('Olivier', "0700")
    assert phonebook.is_consistent()


def test_inconsistent_with_duplicate_entries(phonebook):
    phonebook.add('Monika', "0800")
    phonebook.add('Dominika', "0800")
    assert not phonebook.is_consistent()


def test_inconsistent_with_duplicate_prefix(phonebook):
    phonebook.add('Dominika', "12345")
    phonebook.add('Barbara', "123")
    assert not phonebook.is_consistent()
