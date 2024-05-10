# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from library import library

def main():
    array_of_records = ["record", "record1", "record2", "record3", "record4", "record5"]
    batches = library(array_of_records)
    print(batches)

if __name__ == "__main__":
    main()
