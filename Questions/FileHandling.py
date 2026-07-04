"""Python File Handling Exercises: 30+ Coding Problems with Solutions."""

"""  Write a Python program that accepts a user's name as input and writes it to a file called user.txt."""
# from pathlib import Path
# name=input("Enter the user name : ")
# path=Path("user.txt")
# path.write_text(name)

"""---------------------------------------------------------"""
# name = input("Enter your name: ")

# with open("user.txt", "w") as f:
#     f.write(name)

# print("Name written to user.txt")



""" Write a Python program that opens a file called data.txt and prints its entire contents to the console. """
# with open("user.txt","r") as f:
#     data=f.read()

# print(data)


""" Write a Python program that reads a file called lines.txt and prints each line one at a time using a loop."""

# with open ("user.txt","r") as f:
#     data=f.read()

# for i in data:
#     print(i, end="")


""" Write a Python program that reads all lines from a file called items.txt into a list and prints the list."""
list=[]
with open ("user.txt","r") as f:
    data=f.readlines()

for i in data:
    list.append(i)

print(list)