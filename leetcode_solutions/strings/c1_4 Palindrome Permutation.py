"""
CTCI 1.4
"""
import unittest
from collections import *


def pal_perm(phrase):
    phrase = phrase.replace(' ', '')
    phrase = phrase.lower()
    count = defaultdict(int)

    for c in phrase:
        count[c] += 1
    print(phrase)
    print(count)
    one_found = False

    for v in count.values():
        if v==1:
            if one_found:
                return False
            else:
                one_found=True
        elif v%2!=0:
            return False

    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()