#!/usr/bin/env python

import sys

current_key = None
current_sales = 0.0
current_count = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t", 1)
    sales = float(value)

    if current_key == key:
        current_sales += sales
        current_count += 1
    else:
        if current_key:
            average = current_sales / current_count
            sys.stdout.write("{0}\t{1:.2f}\n".format(current_key, average))
        current_key = key
        current_sales = sales
        current_count = 1

if current_key:
    average = current_sales / current_count
    sys.stdout.write("{0}\t{1:.2f}\n".format(current_key, average))
