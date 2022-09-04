#! /usr/bin/python3

import csv
import sys


reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if line[3] in ("self", "actor", "actress"):
        print("{0}\t{1}".format(line[0], "1"))
