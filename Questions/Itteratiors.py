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
#         yield current  # Yield : it keyword is used to transform a standard function  into a generator functions. : It pause the execution, saves the function's state and output  te values.
#         current +=step

# for num in custom_range(2,10,2):
#     print(num)
      
 
"""
Write an iterator class that takes a string and returns its characters in reverse order.
"""

class Reverse:
    def __init__(self,text):
        self.text=text
        self.index=len(text)-1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index<0:
            raise StopIteration
        
        char = self.text[self.index]
        self.index-=1
        return char
    
for char in Reverse("Hello"):
    print(char,end=" ")
