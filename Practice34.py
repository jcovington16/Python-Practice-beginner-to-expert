#!/usr/local/bin/python3

#Question: The following script throws a NameError in the last line
# saying that c is not defined. Please fix the function so that there is 
# no error and the last line is able to print out the value of c (i.e. 1)

#Bad Code

#def foo():
#    c = 1
#    return c
#foo()
#print(c)

#Soultion
# c needs to be defined as a global variable or the print statement can be removed. 

def foo():
    global c
    c = 1
    return c
foo()
print(c)