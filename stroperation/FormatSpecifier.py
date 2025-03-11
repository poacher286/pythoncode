# Format specifiers = {value:flags} format the value based on what flags are inserted

# :.(number)f = round to that many number of decimal places (fixed point)
# :(number) = allocate that many number of spaces
# :03 = allocate and zero pad that many number of spaces
# :< = left justify
# :> = right justify
# :^ = centre align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive number
# :, = comma separator


price1 = 3234235.141596
price2 = -8234563453.256
price3 = 2334.34

print(f"price1 : ${price1}")
print(f"price2 : ${price2}")
print(f"price3 : ${price3}")

# rounding to decimal places
print(f"price1 : ${price1:.2f}")
print(f"price2 : ${price2:.1f}")
print(f"price3 : ${price3:.3f}")

# allocate number of spaces
print(f"price1 : ${price1:10}")
print(f"price2 : ${price2:10}")
print(f"price3 : ${price3:10}")

# allocate 0 pad that many space
print(f"price1 : ${price1:010}")
print(f"price2 : ${price2:010}")
print(f"price3 : ${price3:010}")

# left align
print(f"price1 : ${price1:<10}")
print(f"price2 : ${price2:<10}")
print(f"price3 : ${price3:<10}")

# right align
print(f"price1 : ${price1:>10}")
print(f"price2 : ${price2:>10}")
print(f"price3 : ${price3:>10}")

# centre align
print(f"price1 : ${price1:^10}")
print(f"price2 : ${price2:^10}")
print(f"price3 : ${price3:^10}")

# indicate plus sign to positive number
print(f"price1 : ${price1:+}")
print(f"price2 : ${price2:+}")
print(f"price3 : ${price3:+}")

# align evenly 
print(f"price1 : ${price1: }")
print(f"price2 : ${price2: }")
print(f"price3 : ${price3: }")

# thousand separator
print(f"price1 : ${price1:,}")
print(f"price2 : ${price2:,}")
print(f"price3 : ${price3:,}")

# you can mix all specifier
print(f"price1 : ${price1:,.2f}")
print(f"price2 : ${price2:+,.2f}")
print(f"price3 : ${price3:+,.2f}")
