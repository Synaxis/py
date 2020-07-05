"""Python Collections (arrays  )

- List is a collection which is ordered and changeable. Allows
duplicate members
-Tuple is a collection which is ordered and UNCHANGEABLE.
Allows
duplicate members
-Set is a collection which is unordered and unindexed. No duplicate members.
-Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""

# List
#A collection which is ordered and changeable. in Python its written wieh brackets[]
thisList = ["apple", "banana", "cherry"]
print(thisList)

# we access the list items by referring to the index number

thisList = ["apple","banana","cherry"]
print("Printing the item n1, not n0 ;)", thisList[1])

#Negative indexing means beginning from the end, -1 refers to the last item
print(thisList[-1])

"""
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.
"""

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:6])

thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[2:])

listaNumeros = ["0","1","2","3","4","5","6","7","8","9"]
print("Printando lista inteira",listaNumeros)

print("Printando de 2 á 5",listaNumeros[2:5])

#check if item exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


listateste = ["carro","arvore","caio","sarah","teste","a",]
if "carro" in listateste:
    print("encontramos carro na lista!!")

#add items using the append() function

thisList = ["apple","banana","grape","pear","pineaple"]
thisList.append("watermelon")
print(thisList)

#The remove() method removes the specified item:

Lista = ["raiz","tronco","caule","folhas"]
Lista.remove("tronco")
print("arvore sem tronco vai cair!", Lista)

#the clear() function clears the entire list

thisList = ["a","b","c","d"]
thisList.clear()
print(thisList)

#Copy List
""" You cannot copy a list by just assigning it like list1 = list2 because this way it will just point to the address
for copying it correctly we use the function copy()
"""
list1 = ["red","green","blue","yellow"]
list2 = list1.copy()
print("list2 is a copy of list1",list2)


#Join Lists
"""There are many ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator."""

list1 = ["1","2","3","4"]
list2 = ["5","6","7","8","9"]
list3 = list1 + list2
print("list3 is the sum of list1 + list2 :O ", list3)
