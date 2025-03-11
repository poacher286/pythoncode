# Dictionary = a collection of {key:value} pairs
#               ordered and changable, No Duplicate

capitals = {"USA" : "Washington D.C.",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA")) # if key not exist then it will give None

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital not exists")    

# capitals.update({"Germany" : "Berlin"})
# capitals.update({"USA" : "New York"}) # update the existing key
# capitals.pop("China") # pop key
# capitals.popitem() # pop last added item
# capitals.clear()

# capitals.keys() # get all keys
# capitals.values() # get all values
items = capitals.items() # items are 2D List of tuples
print(items)
for item in items:
    print(item)

for key, value in items:
    print(f"Key : {key}")    
    print(f"Value : {value}")    

print(capitals)