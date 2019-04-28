import re


#Next call ask how this was formed so I can do it myself


def clean_string(string):
    return re.sub(r'[^a-zA-Z]+', '', string)


def create_list_of_strings(char, amount):
    return [char] * amount
