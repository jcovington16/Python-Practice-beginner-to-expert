#!/usr/local/bin/python3

#Question: Create a function that takes any string as input and 
# returns the number of words for that string. 

def count_words(strng):
    strng_list = strng.split()
    return len(strng_list)

print(count_words("Hello there my friends!"))

def any_string():
    s = input('Enter any string you like: ')
    return s.count()