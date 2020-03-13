import csv
import collections
import itertools

grid = collections.Counter()

with open("follower.csv", "r", newline="") as fp:
    reader = csv.reader(fp)
    for row in reader:
        getName1 = row[0].split('/')
        getName2 = row[1].split('/')

        print(row)
