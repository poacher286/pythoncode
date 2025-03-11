#Indexing - accessing elements of a sequence using [] operator (Indexing operator)
# format [start : end : step]

credit_card_number = "1231-4562-7890-4567"

# print(credit_card_number[3]) # print idx 3
# print(credit_card_number[0, 3]) # print from idx 0 - 3
# credit_card_number[:4] # python assumes start to be 0 if not provided
# credit_card_number[5:] # python assumes end to be last if not provided
# credit_card_number[-1] # Last idx 
# credit_card_number[-2] # same way -2 is second last character and so on

# Last 4 digits
last_4 = credit_card_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_4}")

## step
# credit_card_number[::2] # python assumes start = 0 , end = last and gives you the values in every 2 place
# 0, 2, 4, 6 ...
# print(credit_card_number[::2])

##Reverse a string
# step = -1
credit_card_number = credit_card_number[::-1]
print(credit_card_number)


