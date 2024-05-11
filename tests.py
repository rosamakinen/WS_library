# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import unittest
import string
import random

from library import library

class TestLibrary(unittest.TestCase):
    def test_empty_records(self):
        records = []
        with self.assertRaises(ValueError):
            library(records)

    def test_empty_record(self):
        records = ["test", "", "empty"]
        result = library(records)
        self.assertEqual(len(result[0]), 3, "empty record not processed")

    def test_ok_records_single_batch(self):
        records = []
        for i in range (5):
            record = f"rec{i}"
            records.append(record)
        result = library(records)
        self.assertEqual(len(result[0]), 5, "batch size incorrect")
        self.assertEqual(result[0][0], "rec0", "record obstructed in batch")
        self.assertEqual(result[0][1], "rec1", "record obstructed in batch")
        self.assertEqual(result[0][2], "rec2", "record obstructed in batch")
        self.assertEqual(result[0][3], "rec3", "record obstructed in batch")
        self.assertEqual(result[0][4], "rec4", "record obstructed in batch")

    def test_ok_records_multi_batch(self):
        records = []
        for i in range (505):
            record = f"rec{i}"
            records.append(record)
        result = library(records)

        self.assertEqual(len(result), 2, "output size incorrect")
        self.assertEqual(len(result[0]), 500, "batch size incorrect")
        self.assertEqual(len(result[1]), 5, "batch size incorrect")
        self.assertEqual(result[0][0], "rec0", "record obstructed in batch")
        self.assertEqual(result[0][1], "rec1", "record obstructed in batch")
        self.assertEqual(result[0][2], "rec2", "record obstructed in batch")
        self.assertEqual(result[1][0], "rec500", "record obstructed in batch")
        self.assertEqual(result[1][1], "rec501", "record obstructed in batch")
        self.assertEqual(result[1][2], "rec502", "record obstructed in batch")

    def test_massive_record(self):
        big_string = "x" * 1048599
        records = ["a", "b", "c", big_string]
        result = library(records)
        self.assertEqual(len(result[0]), 3, "big record not discarded")

    def test_over_500_records(self):
        records = []
        for i in range(505):
            res = ''.join(random.choices(string.ascii_uppercase +
            string.digits, k=i))
            records.append(res)
            records.append(res)
            records.append(res)
        result = library(records)

        self.assertEqual(len(result[0]), 500, "batch size incorrect")
        self.assertEqual(len(result[1]), 500, "batch size incorrect")
        self.assertEqual(len(result[2]), 500, "batch size incorrect")
        self.assertEqual(len(result[3]), 15, "batch size incorrect")
        self.assertEqual(len(result), 4, "output size incorrect")

    def test_batch_size(self):
        under_mb_string = "x" * 1000000
        records = [under_mb_string, under_mb_string, under_mb_string, \
                   under_mb_string, under_mb_string, under_mb_string]
        result = library(records)
        
        self.assertEqual(len(result[0]), 5, "batch size incorrect")
        self.assertEqual(len(result), 2, "output size incorrect")

if __name__ == "__main__":
    unittest.main()
