#!/usr/local/bin/python

letters = ["a","b","c","d","e","f","g","h","i","j"]

#Complete the script so that it prints out a list slice containing letters a,c,e,g and i

print(letters[0::2])

#or 

print(letters[::2])

#The double colons tells the script to scipt one and go the next
#The complete syntax of list slicing is [start:end:step]
#When you don't pass a step, Python assumes step is 1. 