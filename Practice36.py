#!/usr/bin/python

# Create a function that takes a text file as input 
# and returns the number of words contained in the text file


import pathlib
import readline

def count_file_words(file_name):
    with open(file_name, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)

print(count_file_words("words1.txt"))