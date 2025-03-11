# collection = single "variable" used to store multiple values
# List = [] ordered and changable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK, No Duplicates
# Tuple = () ordered and unchangable (final), Duplicates OK. FASTER

fruits = ["apple", "banana", "orange", "coconut"]

# print(dir(fruits)) # show all methods for List
# print(help(fruits)) # show detailed function
# print(len(fruits))
# print("apple" in fruits) # boolean value like exist()

# fruits[0] = "pineapple" # update the index
# fruits.append("Pineapple") # add element to List
# fruits.pop() # pop last element
# fruits.remove("apple") # remove element
# fruits.insert(1, "grape") # add element in that index, shift other element to right
# fruits.sort()
# fruits.reverse()
# fruits.clear() # clear list 

# print(fruits.index("apple")) # return index of element
# print(fruits.index("grape")) # ValueError: 'grape' is not in list
# print(fruits.count("apple")) # count element

print(fruits)