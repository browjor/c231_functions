import unittest
from os import remove

from useful_c231.string_manip.preprocessing import remove_space_and_punctuation

class MyTestCase(unittest.TestCase):
    def test_preprocessing(self):
        correct_result = """lookingforrepeatingsubstringscanbetediousandifthecipherismonoalphabeticthenthekasiskitestdoesnthelpusanyhowcanwetellfromthestartwhetherornotoneormorealphabetsarebeingusedtheideahereisthatthefrequencytableofanmscshouldlookliketheoneforstandardenglishjustwiththelettersmatchingdifferentfrequenciesthewayweactuallygoaboutmeasuringthisisalittledifferentfromthisbutitgetsatthesamethingweusetheindexofcoincidence"""
        test = """Looking for repeating substrings can be tedious, and if the cipher is monoalphabetic, then the Kasiski test doesn't help us any. How can we tell from the start whether or not one or more alphabets are being used?

        The idea here is that the frequency table of an MSC should look like the one for standard English, just with the letters matching different frequencies. The way we actually go about measuring this is a little different from this, but it gets at the same thing. We use the Index of Coincidence."""

        self.assertEqual(remove_space_and_punctuation(test), correct_result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
