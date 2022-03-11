import pytest

from src.phonebook import Phonebook


@pytest.fixture
def phonebook(tmpdir):  # tymczasowy folder z pytesta (fixture), sam sie usunie
    """Provides Phonebook with one record"""
    phonebook = Phonebook(tmpdir)

    return phonebook