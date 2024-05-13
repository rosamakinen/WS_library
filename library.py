# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from utils import convert_mb_to_bytes, convert_to_utf8_len

class Library:
    def __init__(self, max_record_size=1, max_batch_size=5, max_records_per_batch=500):
        """
        Initializes the library instance with limits

        Parameters:
        - max_record_size: Maximum size of a single record in megabytes (default: 1 MB).
        - max_batch_size: Maximum size of a batch in megabytes (default: 5 MB).
        - max_records_per_batch: Maximum number of records in a batch (default: 500).
        """
        self._max_record_size_mb = max_record_size
        self._max_batch_size_mb = max_batch_size
        self._max_records_per_batch = max_records_per_batch

        self._max_record_size_bytes = convert_mb_to_bytes(self._max_record_size_mb)
        self._max_batch_size_bytes = convert_mb_to_bytes(self._max_batch_size_mb)

    def library(self, records):
        if not records:
            raise ValueError("cannot process an empty array")

        batch_size = 0
        batch = []
        batches = []

        for record in records:
            record_size = convert_to_utf8_len(record)
            if  batch_size + record_size > self._max_batch_size_bytes \
                or len(batch) + 1 > self._max_records_per_batch:
                batches.append(batch)
                batch = []
                batch_size = 0
            if  record_size <= self._max_record_size_bytes:
                batch.append(record)
                batch_size = batch_size + record_size

        if batch:
            batches.append(batch)
        return batches

# setters and getters #

    def get_max_record_size_mb(self):
        return self._max_record_size_mb

    def get_max_batch_size_mb(self):
        return self._max_batch_size_mb

    def get_max_records_per_batch(self):
        return self._max_records_per_batch

    def set_max_record_size_mb(self, size):
        self._max_record_size_mb = size
        self._max_record_size_bytes = convert_mb_to_bytes(self._max_record_size_mb)

    def set_max_batch_size_mb(self, size):
        self._max_batch_size_mb = size
        self._max_batch_size_bytes = convert_mb_to_bytes(self._max_batch_size_mb)

    def set_max_records_per_batch(self, amount):
        self._max_records_per_batch = amount
