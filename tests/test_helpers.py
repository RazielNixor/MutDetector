import unittest

import helpers


class TestHelpers(unittest.TestCase):
    def test_clean_string_no_digits(self):
        result = helpers.clean_string('asdfASDF')
        self.assertEqual(result, 'asdfASDF')

    def test_clean_string_digits(self):
        result = helpers.clean_string('asdf234234ASDF')
        self.assertEqual(result, 'asdfASDF')

    def test_create_list_of_strings(self):
        result = helpers.create_list_of_strings('a', 5)
        self.assertEqual(result, ['a', 'a', 'a', 'a', 'a'])
