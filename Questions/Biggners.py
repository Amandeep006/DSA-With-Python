"""
Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
"""

# def accept(a,b):
#     if a*b<=1000:
#         return a*b
    
#     else:
#         return a+b
    
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))

# print(f"The result of the given problem is {accept(a,b)}.")


"""
Iterate through the first 10 numbers (0-9). In each iteration, print the current number, the previous number, and their sum.
"""

# pre=0
# for i in range(0,10):
#     if i==0:
#         x=0
#     else:
#         x=i-1
    
#     sum=i+x
#     print(f"THe current {i} and previous number {x}, So Sum of both is {sum}.")


"""
Display only those characters which are present at an even index number in given string.
"""

# str=input("Enter anything :")
    
# print(f"Even indexing string value :{str[::2]}.")


"""
Write a function to remove characters from a string starting from index 0 up to n and return a new string.
"""

# def remove (str,n):
#     return str[n:]

# str=input("Enter the string:")
# n=int(input("Start from the index: "))

# print(f"After removing the {n} character from {str} is {remove(str,n)}.")

"""
Write a program to swap the values of two variables, a and b, without using a third temporary variable.
"""

# a=int(input("Enter the first number :"))
# b=int(input("Enter the second number :"))

# print(f"Before Swapping : a={a} & b={b}.")
# # a=a-b
# # b=b+a
# # a=b-a
# a,b=b,a

# print(f"After Swapping : a={a} & b={b}.")


"""
Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
"""
# n=int(input("Enter the number :"))
# fact=1
# a=n
# while(n>0):
#    fact=fact*n
#    n=n-1


# print(f"Factorial of {a} is {fact}")


"""
Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).
"""
# fruits=['apple','mango','banana','grapes','kiwi']
# del fruits[1]
# fruits.append("Cerry")
# print(fruits )

"""
Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).
"""
# str=input("Enter your string :")
# print(f"Reverse string :{str[::-1]}.")


"""
Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.
"""

# str=input("Enter your string:")
# count=0

# vowels=['a','e','i','o','u','A','E','I','O','U']
# for i in str:
#     # for j in vowels:
#     if i in vowels:
#         # if(i==j):
#             count+=1

# print(f"Number of Vowels in the '{str}' is {count}.")

"""
Given a list of integers, find and print both the largest and the smallest numbers.
"""

# list=[12,45,86,9,23,68,86,5]
# print(f"The minimum number in list : {min(list)}\nThe Maximum number in list : {max(list)}. ")


"""



Write a script that takes a list containing duplicate items and returns a new list with only unique elements.
"""





