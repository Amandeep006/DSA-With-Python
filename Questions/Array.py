"""
Given an integral array nums, return the number of reverse pairs in the array.
a reverse pair is a pair (i,j).
 Where :
* 0<=i<j<nums.length and 
* nums[i]>2>nums[j].
"""

# Firstly apply the brute force.
# def solve(nums):
#     count=0
#     n=len(nums)
#     for i in range(n):
#         for j in range(1,n):
#             if(i<j):
#                 if(nums[i]>2*nums[j]):
#                     count+=1
#                     print(f"Reverse pair : ({i},{j})")                        
            
#     print(f"The total count of the pairs : {count}.")       
   
                
# nums=[1,3,2,3,1]
# solve(nums)


"""
The cumulative sum of an array at index i is defined as the sum of all elements of the array from index 0 to index i.
"""
# num=[1,3,5,7,9]
# sum=0
# cum_sum=[]
# for i in num:
#     sum+=i
#     cum_sum.append(sum)

# print(f"Cumulative Sum: {cum_sum}")

"""
POSITIVE CUMULATIVE SUM
The cumulative sum of an array at index i is defined as the sum of all elements of the array from index 0 to index i.
"""

# num=[1,-2,3,4,-6]
# sum=0
# cum_sum=[]

# for i in num:
#     sum+=i
#     cum_sum.append(sum)

# print(f"Cumulative Sum : {cum_sum}")


"""
Identical twins
For an array of integers nums, an identical twin is defined as pair (i, j) where nums[i] is equal to nums[j] and i < j.
"""

# num=[1,2,2,3,2,1]
# count=0
# show=[]
# index=[]

# for i in range(len(num)-1):
#     for j in range(i+1,len(num)):
#         if num[i]==num[j]:
#             count+=1
#             show.append([num[i],num[j]])
#             index.append((i,j))

# print(f"Number of Identical Twins : {count}")
# print(f"Identical Twins : {show}")

# index=tuple(index) # There is an inbuild function to convert list into tuple.
# print(f"Indexes: {index}")


"""
Given an array of integers, find the elements which have an even number of digits.
"""

# arr = [42,564,5775,34,123,454,1,5,45,3556,23442]

# even_digits = []

# for num in arr:
#     if len(str(abs(num))) % 2 == 0: # abs is used to convert the value for negative to positive number.
#         even_digits.append(num)

# print(even_digits)
# print("Count =", len(even_digits))


"""
2 sum array 
"""
num=[1,5,3,6,2]
target=4

num.sort()
start=0
end=len(num)-1

while start<end:
    if num[start]+num[end]==target:
        print(f"The numbers are {num[start]},{num[end]}.")
        break

    elif num[start]+num[end]<target:
        start+=1

    else:
        end-=1


