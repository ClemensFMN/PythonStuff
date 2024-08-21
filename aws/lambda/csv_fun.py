# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:45:01 2024

@author: x372924
"""


# stupid example of opening a csv file, reading each row, and writing some
# data from the csv into a file (one file for each row)
import csv

# with open('data.csv') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter = ';')
#     next(csvreader, None)
#     for row in csvreader:
#         print(row[0], row[1])
#         fname = 'out_' + row[0] + '.txt'
#         f = open(fname, 'a')
#         f.write(row[1])
#         f.close()


f = open('data.csv')
s = f.readlines()

csvreader = csv.reader(s, delimiter = ';')

for row in csvreader:
    print(row[0], row[1])



