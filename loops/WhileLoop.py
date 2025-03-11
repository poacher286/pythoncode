# While loop = execute some code WHILE some condition remains true

name = input("Enter your name : ")

# if name == "":
#     print("you have not entered your name!!")
# else:
#     print(f"Hello {name}!!")

# changing top while loop until name is not provided 

while name == "":
    print("you have not entered your name!!")
    name = input("Enter your name : ")
print(f"Hello {name}!!")  

