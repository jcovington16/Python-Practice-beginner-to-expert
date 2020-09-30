#!/usr/local/bin/python3

#Question: Here's another similar exercise. What will the following script output? Try to do this mentally if you can.

c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())

# Because 2 was re-defined within the function before the print statement that will be the output. 
# C is a local variable that exists only inside the funtion. The other times c was defined are considered global variables. 