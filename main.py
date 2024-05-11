# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from library import library

def main():
    records = []
    for i in range (501):
        record = f"rec{i}"
        records.append(record)
    print(records)
    try:
        batches = library(records)
    except ValueError:
        print("something went wrong")
    print(batches)

if __name__ == "__main__":
    main()
