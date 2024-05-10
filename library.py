# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import sys

#loop through records, check size, transfer to batch untill batch reaches limit.
def library(records):
    max_record_size = 1048576 #1MB in bytes
    max_batch_size = 5242880 #5MB in bytes
    output = []
    batch = []
    for record in records:
        if sys.getsizeof(batch) + sys.getsizeof(record) > max_batch_size or len(batch) + 1 > 3:
            output.append(batch.copy())
            batch.clear()
        if sys.getsizeof(record) < max_record_size:
            batch.append(record)
    if batch:
        output.append(batch.copy())
    return output
