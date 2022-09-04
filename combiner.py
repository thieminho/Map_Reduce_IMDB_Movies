#! /usr/bin/python3

from operator import itemgetter
import sys

current_film = None
current_count = 0
film = None

for line in sys.stdin:
    line = line.strip()

    film, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_film == film:
        current_count += count
    else:
        if current_film:
            print("{0}\t{1}".format(current_film, current_count))
        current_count = count
        current_film = film
if current_film == film:
    print("{0}\t{1}".format(current_film, current_count))
