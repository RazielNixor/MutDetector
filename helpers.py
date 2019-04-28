import re


# Next call ask how this was formed so I can do it myself


def clean_string(string):
    return re.sub(r'[^a-zA-Z]+', '', string)


def create_list_of_strings(char, amount):
    return [char] * amount


def read_file(file_name):
    with open(file_name) as gene_ref:
        return [line for line in gene_ref]


def read_file_upper(file_name):
    with open(file_name) as gene_ref:
        return [line.upper() for line in gene_ref]
