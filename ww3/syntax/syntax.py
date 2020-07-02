"""syntax in python is a little different
Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentationif 5 > 2:
  print("Five is greater than two!") to indicate a block of code.
"""
#Global varibles
#variables that are created outside of a function

x = "awesome"

def myFunc():
    print("Python is " + x)

myFunc()

#If u create variable w/ same name inside a function, it  will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value

x = "awesome"

def myFunc():
    x = "fantastic"
    print("Python is " + x)

myFunc()

print("Python is " + x) #using the global variable declared earlier
##The global Keyword
#To create a global variable inside a function, you can use the global keyword.


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)