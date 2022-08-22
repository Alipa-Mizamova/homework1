import re

numbers = input("Введите номер машины:  ")
is_valid = re.search(r"([0-9]{2})KG([0-9]{3,4}[A-Z]{3})", numbers)
try:
    if numbers[is_valid.start():is_valid.end()] == numbers:
        print("Номер валидный!")
except:
    print("Номер не валидный!")