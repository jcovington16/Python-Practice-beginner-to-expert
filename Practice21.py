#!/usr/bin/python

d = {"a" : 1, "b" : 2, "c" : 3}

#Filter the dictonary by removing all items with a value of greater than 1
#Expected output: {'a' : 1}

def remove_item(d):
    for value in d.items():
        if value <= 1:
            print(d)
#OR

#for python3
d = { "a" : 1, "b" : 2, "c" : 3}
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)


#for python2
#Use dict.iteritems()
