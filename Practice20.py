#!/usr/bin/python

d = {"a" : 1, "b" : 2, "c" : 3}

#Calculate teh sum of all dictionary values.

results = d["a"] + d["b"] + d["c"]
print(results)

#OR

print(sum(d.values()))