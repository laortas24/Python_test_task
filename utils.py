import json
import string

ALPHABET = string.digits + string.ascii_letters


def serialize_json(path_to_file):
    with open(path_to_file) as f:
        return json.load(f)


def save_json(json_to_save, path_to_file):
    with open(path_to_file, 'w') as f:
        json.dump(json_to_save, f)


def check_for_dict(d):
    if not isinstance(d, dict):
        raise TypeError('dict_to_sort should be type of dict')


def number2base(number, base):
    if number < 0:
        sign = -1
    elif number == 0:
        return ALPHABET[0]
    else:
        sign = 1

    number *= sign
    digits = []

    while number:
        digits.append(ALPHABET[number % base])
        number = number // base

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)
