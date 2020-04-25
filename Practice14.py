#!/usr/local/bin/python

a = ["1", 1, "1", 2]

#Complete the script so that it removes duplicate items from list a.

a = list(set(a))

#or

print(list(set(a)))

#or

from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

#OderedDict keeps the varaible in order. List function don't respect the order of which the variable list is in.
