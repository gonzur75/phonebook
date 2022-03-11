from src.phonebook.phonebook import clean_phone_number


def test_clean_phone_number():
    assert "0392987230" == clean_phone_number("039 298-72-30")

