#!/usr/local/bin/python3

#Question: What will the follownig script output? Please try to do this mentally if you can.

c = 1 
def foo():
    return c
c = 3
print(foo())

# 3 will be printed to the screen. The variable was defined after the return statment, 
# so there's nothing that c will return. Also 1 was defined, but with python you can  
# change a variable easily. 