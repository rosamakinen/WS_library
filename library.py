# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

#loop through records, check size, transfer to batch untill batch reaches limit.
#check for empty records

MAX_RECORD_SIZE = 1048576 #1MB in bytes
MAX_BATCH_SIZE = 5242880 #5MB in bytes
MAX_RECORDS_PER_BATCH = 500

def library(records):
    if not records:
        raise ValueError("trying to process an empty array")

    batch_size = 0
    batch = []
    batches = []

    for record in records:
        record_size = len(record.encode('utf-8'))
        if  batch_size + record_size > MAX_BATCH_SIZE or len(batch) + 1 > MAX_RECORDS_PER_BATCH:
            batches.append(batch.copy())
            batch.clear()
            batch_size = 0
        if  record_size <= MAX_RECORD_SIZE:
            batch.append(record)
            batch_size = batch_size + record_size
        else:
            continue

    if batch:
        batches.append(batch.copy())
    return batches
