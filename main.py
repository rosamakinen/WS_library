# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from library import library

def main():
    records = []
    for i in range (20):
        record = f"record{i}"
        records.append(record)
    print(records)
    batches = library(records)
    print(batches)

if __name__ == "__main__":
    main()
