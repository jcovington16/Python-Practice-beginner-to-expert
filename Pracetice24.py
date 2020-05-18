#!/usr/bin/python

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

for key, value in d.items():
    print(key, "has value", value)


pprint("b has a value " + d.items('b'))
pprint("a has a value " + d.items('c'))
pprint("c has a value " + d.items('a'))