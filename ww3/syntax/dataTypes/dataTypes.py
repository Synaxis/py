"""Built-in Data Types
Python has the following data types built-in by default, in these categories:

Text type: str
Numeric Types: int,float,complex
Sequence Types: list,tuple,range
Mapping Type: dict
Set Types: set,frozenset
Boolean Type bool
Binary Types: bytes,bytearray,memoryview

Getting the Data Type
You can get the data type of any object by using the type() function:
"""
x = 5
print(type(x))

#in python, the data type is set when you assign a value to a variable
x = ("apple", "banana", "cherry")	 #tuple
x = b"Hello"	#bytes
x = bytearray(5)	#bytearray
x = memoryview(bytes(5))	#memoryview
x = {"apple", "banana", "cherry"}	 #set