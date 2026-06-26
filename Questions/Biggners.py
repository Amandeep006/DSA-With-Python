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


#fifth commit
"""
Write a script that takes a list containing duplicate items and returns a new list with only unique elements.
"""
# data =[1,2,2,3,3,4,4,5,5,5,5]
# unique=list(set(data))
# print(f"THe unique list : {unique}")



"""
Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.
""" 

# def check(list):
#     n=list[-1]
#     if(list[0]==n):
#         return True
#     elif(list[0]!=n):
#         return False
    

# list=[10,20,30,40,10,30]
# print(f"The first and last number is list is {check(list)}")


"""
Iterate through a given list of numbers and print only those numbers which are divisible by 5.
"""

# list=[10,20,33,46,55]

# for i in list:
#     if i%5==0:
#         print(i, end=" ")


"""
Write a program to find how many times the substring “Emma” appears in a given string.
"""

# str="Emma is good developer. Emma is a writer"
# print(f"The Emma word in str have {str.count("Emma")} times.")


"""
Print the following pattern where each row contains a number repeated a specific number of times based on its value.
1
22 
333
4444
"""
# n=int(input("Enter the size: "))
# for i in range(n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print(" ")


"""
Write a program to check if a given number is a palindrome (reads the same forwards and backwards).
"""
# str=input("Enter your word: ").title()
# pal=str[::-1].title()

# if(str==pal):
#     print(f"The given string {str} is Palindrome.")

# else:
#     print(f"The given string {str} is not Palindrome.")

"""
Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.
"""
# list1=[10,20,25,30,35]
# list2=[40,45,50,65,70]
# list3=[]

# for i in list1:
#     if i%2!=0:
#         list3.append(i)

# for j in list2:
#     if j%2==0:
#         list3.append(j)

# print(f"The commbined list of 1 and 2 : {list3}.")


"""
 Write a program to extract each digit from an integer in the reverse order.
"""

# a=int(input("Enter any number:"))
# while(a>0):
#     r=a%10
#     a=a//10
#     print(r, end="")

# sixth commit


"""
Calculate income tax for a given income based on these rules:

First $10,000: 0% tax
Next $10,000: 10% tax
Remaining income: 20% tax
"""

# income=int(input("Enter your income : ")) 

# tax=0
# first_half=income-10000
# sec_tax=(10000*10)//100
# second_half=first_half-10000
# remain_tax=(second_half*20)//100

# total_tax=sec_tax+remain_tax
# print(f"The Total Pay able tax is {total_tax}.")

# income = 45000
# tax_payable = 0
# print("Given income:", income)

# if income <= 10000:
#     tax_payable = 0
# elif income <= 20000:
#     # Tax on first 10k is 0. Tax on the rest is 10%
#     tax_payable = (income - 10000) * 10 / 100
# else:
#     # First 10,000 (0% tax)
#     # Next 10,000 (10% tax = 1,000)
#     tax_payable = 0 + (10000 * 10 / 100) 
#     # Remaining income (20% tax)
#     tax_payable += (income - 20000) * 20 / 100

# print("Total income tax to pay is", tax_payable)
 

"""
Print a multiplication table from 1 to 10 in a formatted grid.
"""

# for i in range(1,11):
#     for j in range(1,11):
#         print(j*i, end=" ")
#     print("")


"""
Print a downward half-pyramid pattern using stars (*)
*****
****
***
**
*
"""

n=int(input("Enter the size:"))
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")

    print("")

    # seventh commit 