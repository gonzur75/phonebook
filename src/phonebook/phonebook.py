import os.path


class Phonebook:
    def __init__(self, cache_directory):
        self.numbers = {}
        self.filename = os.path.join(cache_directory, 'phonebook.txt')
        self.cache = open(self.filename, 'w')

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
                    continue
                if clean_phone_number(number1).startswith(clean_phone_number(number2)):
                    return False
        return True


    def names(self):
        return self.numbers.keys()

    def clear(self):
        self.cache.close()
        os.remove(self.filename)


def clean_phone_number(phone_number):
    to_remove = ["-", " "]
    for c in to_remove:
        phone_number = phone_number.replace(c, "")
    return phone_number.replace(" ", "").replace("-", "")