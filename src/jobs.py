from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as f:
        arr = []
        file = csv.DictReader(f, delimiter=",", quotechar='"')
        for files in file:
            arr.append(files)
        return arr
