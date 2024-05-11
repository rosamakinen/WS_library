# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

#loop through records, check size, transfer to batch untill batch reaches limit.
#check for empty records 
def library(records):
    max_record_size = 1048576 #1MB in bytes
    max_batch_size = 5242880 #5MB in bytes
    max_records_per_batch = 500
    batch_size = 0
    batch = []
    batches = []
    for record in records:
        record_size = len(record.encode('utf-8'))
        if  batch_size + record_size > max_batch_size or len(batch) + 1 > max_records_per_batch:
            batches.append(batch.copy())
            batch.clear()
            batch_size = 0
        if  record_size <= max_record_size:
            batch.append(record)
            batch_size = batch_size + record_size
        else:
            continue
    if batch:
        batches.append(batch.copy())
    return batches
