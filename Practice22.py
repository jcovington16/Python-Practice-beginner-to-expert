#!/usr/bin/python

#pprint is a python built-in module which is used to print out well formatted views of databases 

from pprint import pprint


d = {"a" : list(range(1,11)), "b" : list(range(11,21)), "c" : list(range(21,31))}
pprint(d)