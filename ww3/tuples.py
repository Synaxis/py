#negative indexing 
#negative indexing means beggining from the end
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


#Change Tuple Values

"""once a tuple is created , you cannot change its values. Tuples are unchangeable, or immutable
as it also is called. But you can convert the tuple into a list , and convert it back to a tuple after the change"""

x = ("apple","mango","banana","pear","grape")
y = list(x) # a list with the tuple inside
y[1] = "kiwi"
x = tuple(y)
print(x)

#Loop through a tuple

# you can loop with a for loop like any other list
thistuple = ("apple","banana","pear")
for x in thistuple:
    print(x)

#Check if item Exists
# to determine if a specified item is in the tuple

thistuple = ("apple","banana","car","red")
if "apple" in thistuple:
    print(" yes we found apple inside the tuple list")

#Tuple Length
#To determine how many itesm use the , use the len() method:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Create tuple with 1 item ( you NEED to use the , comma)
thistuple = ("banana",)
print(type(thistuple))

#NOT a tuple
thistuple = ("banana")
print(type(thistuple))