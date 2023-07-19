import sys
import numpy
import quandl
import pandas

import re


df = quandl.get("WIKI/GOOGL")
# df.set_printoptions(threshold=sys.maxsize)


def print_full(x):
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.width', 2000)
    pandas.set_option('display.float_format', '{:20,.2f}'.format)
    pandas.set_option('display.max_colwidth', None)
    return x
    # pandas.reset_option('display.max_rows')
    # pandas.reset_option('display.max_columns')
    # pandas.reset_option('display.width')
    # pandas.reset_option('display.float_format')
    # pandas.reset_option('display.max_colwidth')


# numpy.set_printoptions(threshold=numpy.inf)
# print(print_full(df))

# c = [i for i in range(100)]


s = open("stocking-google.txt", "r")
c = re.sub("\s+", ",", s.read().strip())
# print(c)

f = open("stocking-google2.csv", "a")
f.write(str(c))
f.close()

# s.close()

# df = pandas.read_csv("stocking-google2.csv")

# print(df.head())
