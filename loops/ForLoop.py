# for loop = execute a block of code a fixed number of times 
#       you can itterate over a range, string, sequence etc
#       anything which can be itteratable

# for x in range(1, 11): # 1 is inclusive.  11 is exclusive
#     print(x)

# for x in reversed(range(1, 11)): # 1 is inclusive.  11 is exclusive
#     print(x)
    
# for x in reversed(range(1, 11, 2)): # count by 2
#     print(x)    

for x in range(11, 1, -1): # count backwards 1 is exclusive
    print(x)

# itterate over string
# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

for x in range(1, 20):
    if x == 13:
        continue # skip that point
    else:
        print(x)

for x in range(1, 20):
    if x == 13:
        break # break that point
    else:
        print(x)        