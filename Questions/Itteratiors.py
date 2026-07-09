"""Python Iterators and generators."""

"""
Create a generator function that yields the squares of numbers from 1 to n.
"""
# for i in range(1,6):
#     print(i**2, end=" ")

"""
Write a class-based iterator that returns even numbers up to a specified limit.
"""

# class EvenIterator:
#     def __init__(self,num):
#         self.num=num
#         self.current=0
    
#     def __iter__(self): # __iter__() is a special dunder method that return an iterator object for a collection.
#         return self
    
#     def __next__(self): #  __next__() method is a specical method in pyhton used to retrieve the next item form an iterator.
#         if self.current>self.num:
#             raise StopIteration # raise keyword: the raise keyword raises an exception and immeditaely stops the naormal execution of the program.
#         # StopIteration : It is a built-in python exception used as a signal to indicate that an iterator has no further items to return.

#         value =self.current
#         self.current+=2
#         return value
    
# for num in EvenIterator(10):
#         print(num, end=" ")


"""
Re-implement a simplified version of the range() function using a generator.
"""
# nums=range(2,10,2)

# for num in nums:
#     print(num, end=" ")

# """--------------------"""
# def custom_range(start, stop, step):
#     current=start

#     while current<stop:
#         yield current  # Yield : it keyword is used to transform a standard function  into a generator functions. : It pause the execution, saves the function's state and output the values.
#         current +=step

# for num in custom_range(2,10,2):
#     print(num)
      
 
"""
Write an iterator class that takes a string and returns its characters in reverse order.
"""

# class Reverse:
#     def __init__(self,text):
#         self.text=text
#         self.index=len(text)-1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index<0:
#             raise StopIteration
        
#         char = self.text[self.index]
#         self.index-=1
#         return char
    
# for char in Reverse("Hello"):
#     print(char,end=" ")


"""
 Create a generator that takes a string and yields only the vowels found in it.
"""

# def vowels(text):
        
#     vowels="aeiou"

#     for char in text:
#         if char.lower() in vowels:
#             yield char


# for vowel in vowels("hello! world"):
#     print(vowel, end=" ")


"""
Write a generator expression (one-liner) that yields powers of 2 (e.g., 1, 2, 4, 8…).
"""


# def power(n):
#     for i in range(n):
#         yield 2**i


# for num in power(8):
#     print(num, end=" ")

"""
Write a generator to produce the first n numbers in the Fibonacci sequence, where each number is the sum of the two preceding ones.
"""

# def fibonacci(num,a,b):
#     print(0,1, end=" ")
#     while(num>0):
#         c=a+b
#         yield c
#         a=b
#         b=c

#         num-=1


# n=int(input("Enter the sizee of fibonacci series : "))
# for num in fibonacci(n-2,0,1):
#     print(num, end=" ")
   

"""
Create a generator that starts at 1 and counts up infinitely (don’t run this without a break condition!).
"""

def count(n):
    i=1
    while True:
        if (i==n+1):
            break
        yield i
        i=i+1

        

for i in count(9):
    print(i, end=" ")
        
