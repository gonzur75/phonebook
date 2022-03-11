import csv
import os

import pytest


@pytest.mark.slow
def test_large_file(phonebook):
    with open(os.path.join('sample_data', 'sample.csv')) as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            name = row['Name']
            number = row['Phone Number']
            phonebook.add(name, number)
    assert phonebook.is_consistent()
