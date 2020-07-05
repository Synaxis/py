"""Set
A set is a collection  unordered and unindexed. 
In Python sets are written with curly brackets.
"""
newSet = {"a","b","c"}
print(newSet)

"""Access Items
You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
"""

newSet = {"a","b","c"}
for x in newSet:
    print(x)
if "a" in newSet:
    print("we found a")