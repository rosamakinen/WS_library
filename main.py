# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from library import Library

def main():
    my_library = Library()
    records = []
    for i in range (501):
        record = f"rec{i}"
        records.append(record)
    try:
        batches = my_library.library(records)
    except ValueError:
        print("something went wrong")
    print(batches)

if __name__ == "__main__":
    main()