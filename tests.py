# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import unittest
import string
import random

from library import Library

class TestLibrary(unittest.TestCase):
    def test_empty_records(self):
        my_library = Library()
        records = []
        with self.assertRaises(ValueError):
            my_library.library(records)

    def test_empty_record(self):
        my_library = Library()
        records = ["test", "", "empty"]
        result = my_library.library(records)
        self.assertEqual(len(result[0]), 3, "empty record not processed")

    def test_ok_records_single_batch(self):
        my_library = Library()
        records = []
        for i in range (5):
            record = f"rec{i}"
            records.append(record)
        result = my_library.library(records)
        self.assertEqual(len(result[0]), 5, "batch size incorrect")
        self.assertEqual(result[0][0], "rec0", "record content changed")
        self.assertEqual(result[0][1], "rec1", "record content changed")
        self.assertEqual(result[0][2], "rec2", "record content changed")
        self.assertEqual(result[0][3], "rec3", "record content changed")
        self.assertEqual(result[0][4], "rec4", "record content changed")

    def test_ok_records_multi_batch(self):
        my_library = Library()
        records = []
        for i in range (505):
            record = f"rec{i}"
            records.append(record)
        result = my_library.library(records)
        self.assertEqual(len(result), 2, "output size incorrect")
        self.assertEqual(len(result[0]), 500, "batch size incorrect")
        self.assertEqual(len(result[1]), 5, "batch size incorrect")
        self.assertEqual(result[0][0], "rec0", "record content changed")
        self.assertEqual(result[0][1], "rec1", "record content changed")
        self.assertEqual(result[0][2], "rec2", "record content changed")
        self.assertEqual(result[1][0], "rec500", "record content changed")
        self.assertEqual(result[1][1], "rec501", "record content changed")
        self.assertEqual(result[1][2], "rec502", "record content changed")

    def test_massive_record(self):
        my_library = Library()
        big_string = "x" * 1048599
        records = ["a", "b", "c", big_string]
        result = my_library.library(records)
        discarded = my_library.get_discarded_records()
        self.assertEqual(len(result[0]), 3, "big record not discarded")
        self.assertEqual(len(discarded), 1, "big record not saved to discarded")

    def test_over_500_records(self):
        my_library = Library()
        records = []
        for i in range(505):
            res = ''.join(random.choices(string.ascii_uppercase +
            string.digits, k=i))
            records.append(res)
            records.append(res)
            records.append(res)
        result = my_library.library(records)
        self.assertEqual(len(result[0]), 500, "batch size incorrect")
        self.assertEqual(len(result[1]), 500, "batch size incorrect")
        self.assertEqual(len(result[2]), 500, "batch size incorrect")
        self.assertEqual(len(result[3]), 15, "batch size incorrect")
        self.assertEqual(len(result), 4, "output size incorrect")

    def test_batch_size(self):
        my_library = Library()
        under_mb_string = "x" * 1000000
        records = [under_mb_string, under_mb_string, under_mb_string, \
                   under_mb_string, under_mb_string, under_mb_string]
        result = my_library.library(records)
        self.assertEqual(len(result[0]), 5, "batch size incorrect")
        self.assertEqual(len(result), 2, "output size incorrect")

    def test_setting_limits(self):
        my_library = Library(1, 1, 5)
        records = []
        for i in range (19):
            record = f"rec{i}"
            records.append(record)
        result = my_library.library(records)
        self.assertEqual(my_library.max_batch_size_mb, 1, "batch size set incorrectly")
        self.assertEqual(my_library.max_record_size_mb, 1, "record size set incorrectly")
        self.assertEqual(my_library.max_records_per_batch, 5, "records per batch set incorrectly")
        self.assertEqual(len(result), 4, "output size incorrect")

if __name__ == "__main__":
    unittest.main()
