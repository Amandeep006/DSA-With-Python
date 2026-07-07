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
# list=[]
# with open ("user.txt","r") as f:
#     data=f.readlines()

# for i in data:
#     list.append(i)

# print(list)


"""
Write a Python program that appends the sentence This is a new line. to an existing file called notes.txt without overwriting its current content.
"""
# with open ("user.txt","a") as f:
#     data=f.write("This is a new line.")

# print(data)



"""
Write a Python program that clears all content from an existing file called temp.txt, leaving it as an empty file.
"""

# with open ("user.txt","w") as file:
#     pass     

# print("The file is  going to empty.")


"""
 Write a Python program that creates a new file called output.txt and writes three lines of text to it.
"""

# with open ("Output.txt","w" ) as f:
#     f.write("First line \nSecond line \nthird line.")

# print("Your New File is  created.")

"""
Write a Python program that checks whether a file called data.txt exists in the current directory and prints an appropriate message based on the result.
"""

# from pathlib import Path

# path = Path("Output.txt")

# if path.exists():   # path.exits()- it is used to check our file is exits or not in the directory.
#     print("Your file is exits in the directory .")

# else:
#     print("This file is not exits in this.")


"""
 Write a Python program that attempts to open a file called missing.txt and gracefully handles the case where the file does not exist using a try-except block.
"""

# from pathlib import Path

# path=Path("message.txt")

# try:
#    data= path.read_text(encoding="utf-8")
# except FileNotFoundError:
#    print(f"Sorry, the file {path} does not exits.")
   

"""
 Write a Python program that opens a file called data.txt and counts the total number of lines it contains.
"""
# count=0
# with open ("Output.txt") as f:
#     datas=f.readlines()

# for data in datas:
#     count+=1

# print(f"{count} Total lines in this file.")


"""
Write a Python program that reads a file called data.txt and counts the total number of words across all its lines.
"""
count=1
with open ("Output.txt") as f:
    data=f.read()

words=data.split()

print(f"{count} number or words are prsent in the whole file.")