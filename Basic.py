"""Using the Break statement."""
# limit=10
# cursum=0

# while True:
#     num=int(input())
#     if cursum+num>limit:
#         print(cursum,"limit reached")
#         break

#     cursum+=num


"""Pattern printing questions."""
# 1 2 3
# 1 2 3

# n=int(input("Enter number of rows:"))
# m=int(input("Enter number of column:"))

# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(j,end=" ")
#     print("\n")


# 1
# 12
# 123
# 1234

# n=int(input("Enter the size:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")

#     print("")


    
#     *
#    **
#   ***
#  ****
# ***** 


# n=int(input("Enter the size:"))
# for i in range (n,0,-1):
#     for j in range (1,n+1):
#         if(j<i):
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print("")    
    


"""Find the Factorial of a number with using Recursion """


# def fact(n):
#     if n==0 or n==1:
#         return 1
    
#     return n* fact(n-1)

# print(fact(5))


    

"""Fibonnaci series using Recursion."""

def fibb(n):
    if n==1 or n==2:
        return 1
    
    return fibb(n-1)+ fibb(n-2)


print(fibb(6))


"""Write a program to take a size a list from the user and also take those elements and print the sum of all numbers."""

# n=int(input("Enter the size of list:"))
# list=[]
# sum=0
# for i in range(n):
#     num=int(input("Enter the elements: "))
#     list.append(num)
#     sum+=num

# print(list)
# print(f"The sum of all numbers is {sum}")


"""Find the maximum and minimum values from the list."""

# n=int(input("Enter the size of list:"))
# list=[]
# for i in range(n):
#     num=int(input(f"Enter the element {i+1}: "))
#     list.append(num)

# a=min(list)
# b=max(list)
# print(f"The list is :{list}")
# print(f"The minimum value is {a} and the maximum value is {b}. ")


"""Find the mean, median and mode from the list."""
# import  statistics

# n=int(input("Enter the size of list:"))
# list=[]
# for i in range(n):
#     num=int(input(f"Enter the element {i+1} :"))
#     list.append(num)

# mn= statistics.mean(list)
# md= statistics.median(list)
# mo= statistics.mode(list)

# print(f"The  list : {list}")
# print(f"The mean, median and mode of list are {mn},{md} and {mo} respectively.")



"""Print the 3 by 3 matrix."""
# list=[[1,2,3],[4,5,6],[7,8,9]]
# print(list[0][1])  

# rw=int(input("Enter the Size of Row:"))
# clm=int(input("Enter the size of Column:"))
# list=[]

# for i in range(rw):
#     num=input(f"Enter the element {i+1}:").split()
#     for j in range(clm):
#         num[j]=int(num[j])
#     list.append(num)

# print(list)
    

"""Firstly create a 3X3 matrix and then print the diagonal elements of matrix."""

# rw=int(input("Enter the Size of Rows:"))
# clm=int(input("Enter the Size of Column:"))

# list=[]
# dia=[]
# for i in range(rw):
#     num=input(f"Enter the element of Row{i+1}: ").split()
#     for j in range(clm):
#         num[j]=int(num[j])
        
#     list.append(num)
# print(list)

# # Print the diagonal elements of the matrix.
# for i in range(rw):
#     for j in range(clm):
#         if(i==j):
#             dia.append(list[i][j])
        
# print(dia)

"""Write a program to Transpose of the matrix."""
# rw=int(input("Enter the size of Rows:"))
# clm=int(input("Enter the size of Columns:"))

# list=[]
# for i in range(rw):
#     num=input(f"Enter the elements of Row{i+1}:").split()
#     for j in range(clm):
#         num[j]=int(num[j])
    
#     list.append(num)

# # Transpose of the matrix.

# for i in range(rw):
#     for j in range(clm):
#         if(j>i):
#             temp=list[i][j]
#             list[i][j]=list[j][i]
#             list[j][i]=temp 
           

# print(list)

"""Identify the given string is palindrome or nor."""

str=input("Enter your word: ").title()
pal=str[::-1].title()

if(str==pal):
    print(f"The given string {str} is Palindrome.")

else:
    print(f"The given string {str} is not Palindrome.")
# Fourth commit 