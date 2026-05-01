set1={1,2,3,4,5,5}
list= set([4,5,6,4,7,5]) # converting a list into  a set 

print(set1) #output: {1, 2, 3, 4, 5}
print(list) #output: {4, 5, 6, 7}

print("After adg new elements-----------------")
set1.add(6)
list.add(8)
print(set1) #{1, 2, 3, 4, 5, 6}
print(list) #{4, 5, 6, 7, 8}

print("After removing ==============")
set1.remove(2)
list.remove(4)
print(set1) #{1, 3, 4, 5, 6}
print(list) #{5, 6, 7, 8}

print("Checking particular element in a set------------------->")
print(10 in set1) #False because it's not in the set 
print(7 in list) # True because it's in the set 
print(7 not in list) # False it's in the set

print("Basic set operations------------------------->")
print(set1 |list) # union
print(set1 & list) # intersaction
print(set1 - list) #differnce