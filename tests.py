# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import unittest

from library import Library

#NOTES:
#does the abstracted assertion mean that we would always
#want to do a specific set of tests for the result?
#like knowing the expected size of the output array and the contents
#we could always test the same set?

#NEW IDEA, what if we had a keyword/ constant for the expected data-type
#and then based on the data type we created either a dictionary set or
#an array! commented out code is dumb

class TestLibrary(unittest.TestCase):
    @staticmethod
    def create_test_records(num_of_records):
        # records = []
        # for i in range(num_of_records):
        #     records.append(f"rec{i}")

        # dict
        records = {}
        for i in range(num_of_records):
            records[i] = f"rec{i}"
        return records

    @staticmethod
    def add_empty_record_to_records(records):
        # records.append("")
        key = len(records)
        records[key] = ""

    @staticmethod
    def add_massive_record_to_records(records):
        over_mb_record = "x" * 10000000
        # records.append(over_mb_record)
        key = len(records)
        records[key] = over_mb_record

    def test_empty_records(self):
        my_library = Library()
        records = self.create_test_records(0)
        result = my_library.process_records_to_batches(records)
        self.assertEqual(len(result), 0, "batch size incorrect")

    def test_empty_record(self):
        my_library = Library()
        records = self.create_test_records(1)
        self.add_empty_record_to_records(records)
        result = my_library.process_records_to_batches(records)
        self.assertEqual(len(result[0]), 2, "empty record not processed")

    def test_ok_records_single_batch(self):
        my_library = Library()
        records = self.create_test_records(5)
        result = my_library.process_records_to_batches(records)
        self.assertEqual(len(result[0]), 5, "batch size incorrect")
        self.assertEqual(result[0][0], "rec0", "record content changed")
        self.assertEqual(result[0][1], "rec1", "record content changed")
        self.assertEqual(result[0][2], "rec2", "record content changed")
        self.assertEqual(result[0][3], "rec3", "record content changed")
        self.assertEqual(result[0][4], "rec4", "record content changed")

    def test_ok_records_multi_batch(self):
        my_library = Library()
        records = self.create_test_records(505)
        result = my_library.process_records_to_batches(records)
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
        records = self.create_test_records(3)
        self.add_massive_record_to_records(records)
        result = my_library.process_records_to_batches(records)
        self.assertEqual(len(result[0]), 3, "record larger than limit was saved")

    def test_over_500_records(self):
        my_library = Library()
        records = self.create_test_records(1515)
        result = my_library.process_records_to_batches(records)
        self.assertEqual(len(result[0]), 500, "batch size incorrect")
        self.assertEqual(len(result[1]), 500, "batch size incorrect")
        self.assertEqual(len(result[2]), 500, "batch size incorrect")
        self.assertEqual(len(result[3]), 15, "batch size incorrect")
        self.assertEqual(len(result), 4, "output size incorrect")

    def test_batch_size(self):
        my_library = Library()
        records = self.create_test_records(501)
        result = my_library.process_records_to_batches(records)
        self.assertEqual(len(result[0]), 500, "batch size incorrect")
        self.assertEqual(len(result), 2, "output size incorrect")

    def test_setting_limits(self):
        my_library = Library(1, 1, 5)
        records = self.create_test_records(20)
        result = my_library.process_records_to_batches(records)
        self.assertEqual(my_library.get_max_batch_size_mb(), 1, "batch size set incorrectly")
        self.assertEqual(my_library.get_max_record_size_mb(), 1, "record size set incorrectly")
        self.assertEqual(my_library.get_max_records_per_batch(), 5, "records per batch set incorrectly")
        self.assertEqual(len(result), 4, "output size incorrect")

    def test_setting_limits_with_setters(self):
        my_library = Library()
        my_library.set_max_record_size_mb(1)
        my_library.set_max_batch_size_mb(1)
        my_library.set_max_records_per_batch(2)
        records = self.create_test_records(20)
        result = my_library.process_records_to_batches(records)
        self.assertEqual(my_library.get_max_batch_size_mb(), 1, "batch size set incorrectly")
        self.assertEqual(my_library.get_max_record_size_mb(), 1, "record size set incorrectly")
        self.assertEqual(my_library.get_max_records_per_batch(), 2, "records per batch set incorrectly")
        self.assertEqual(len(result), 10, "output size incorrect")

if __name__ == "__main__":
    unittest.main()
