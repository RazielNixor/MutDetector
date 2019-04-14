import re


def clean_string(string):
    return re.sub(r'[^a-zA-Z]+', '', string)


def create_list_of_strings(char, amount):
    return [char] * amount
