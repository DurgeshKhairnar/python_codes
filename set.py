

# myList = [10,20,30,10,40,50,10]

# mySet = set(myList)

# mySet.add(100)

# mySet.discard(60)

# mySet.update([70,60])

# mySet.pop()

# print(mySet)


a = {1,2,3,4}

b = {4,5,6,7}

print(a | b) # unique element

print(a & b) # comman element

print(b - a) # element in the first set only 

print(a ^ b) # element not comman

print(a.union(b)) # unique element
 
print(b.intersection(a)) # all element

print(a.issubset(b)) # check if all element inside in another arrey

print(a.isdisjoint(b)) # check comman elemnt 