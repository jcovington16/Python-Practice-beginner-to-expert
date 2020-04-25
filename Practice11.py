#!/usr/local/bin/python

#Create a script that generates and prints a list of numbers from 1 to 20. Don't create the list manually

my_range = range(1,21)
print(list(my_range))


#range() is a python built-in function that generates a range of integers. However, range()
#creates a Python range object. To get a real list object you need to use the list() function
#to convert the range object into a list object.