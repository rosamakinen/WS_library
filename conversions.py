# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

BYTES_PER_KILOBYTE = 1024
BYTES_PER_MEGABYTE = BYTES_PER_KILOBYTE * BYTES_PER_KILOBYTE

def convert_mb_to_bytes(megabytes):
    return megabytes * BYTES_PER_MEGABYTE

def convert_to_utf8_len(string):
    return len(string.encode('utf-8'))
