import sys
import numpy
import quandl

numpy.set_printoptions(threshold=sys.maxsize)

df = quandl.get("WIKI/GOOGL")
# print(df.head())

# c = [i for i in range(100)]

f = open("stocking-google.txt", "a")
f.write(str(df))
f.close()
