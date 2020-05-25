#!/usr/bin/python3

#Why do we get an error and how do we fix it?

#def foo(a=2,b):
    #retrun a + b

#fix

def foo(b, a=2):
    return a + b
print(foo(3))