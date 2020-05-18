#!/usr/bin/python

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

for key, value in d.items():
    print(key, "has value", value)


print("b has a value " + d.items('b'))
print("a has a value " + d.items('c'))
print("c has a value " + d.items('a'))