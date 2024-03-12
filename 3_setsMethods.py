a = {1,2,3,4,5,1,2,3,4,5}
# print(type(a))
print(a)
# it does not take the repetative function like here 1,2,3,4,5 are print only once
#set is the collection of non repetative element
a.add(6)
# print(a)

a.add((7,8,9))#tuple

# we cannot add list and dictionary
print(len(a))

# a.remove()
print(a.pop())
a.update({7, 8})  
print(a)
a.remove(3)       
a.discard(4)     # Removes the specified element if it exists, without raising an error
c = 5 in a  
print(c)

b = {2,4,6,8,0}
d= a.intersection(b)
print(d)          #common elements between
e = a.union(b)    #common  + extra from set A to B
print(e)
print("ooooooooooooooooooooooo")
f = a.symmetric_difference(b) #elements present in either sets but not common
print(f)
g = a.issubset(b) #checks whether all elements of set A are present in Set B or not
print(g)
print("++++++++++++++++++++")
h = a.issuperset(b)
print(h)           #Checks whether all elements of Set B are present in Set A or not
i = b.isdisjoint(a) #returns True if two sets have no intersection
print(i)
j = a - b         #Returns a set that contains the difference between two sets (elements which are in A but not in B).
# j = a - b         #return the difference of two sets
# k = b | a         # return union of two sets
# l = a & b         # return intersection of two sets                             SYMBOLS
# m = a ^ b         # returns symmetric difference of two sets
# n = ~a            # bitwise complement operator

t = a.copy()     # returns a copy of the set
print(t)
u = a.clear()    # remove all items from S.

print ("---")
f = a.difference(b)#elements which are in a but not in b

print(a)
