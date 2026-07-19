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
# num=[1,5,3,6,2]
# target=4

# num.sort()
# start=0
# end=len(num)-1

# while start<end:
#     if num[start]+num[end]==target:
#         print(f"The numbers are {num[start]},{num[end]}.")
#         break

#     elif num[start]+num[end]<target:
#         start+=1

#     else:
#         end-=1


"""
3 Sum array
"""

# num=[1,5,3,9,7,6]
# target=9
# start=0
# end=len(num)-1
# mid=start+1

# while True:
#     current=num[start]+num[mid]+num[end]
#     if current==target:
#         print(num[start],num[mid],num[end])
#         break

#     elif current<target:
#         start+=1

#     else:
#         end-=1

"""
DNF Algorithm
"""

# def DNF(num):
#     low=0
#     high=len(num)-1
#     mid=0

#     while mid<high:
#         if num[mid]==0:
#             Swap(low,mid,num)
#             # num[low],num[mid]=num[mid],num[low]
#             mid+=1
#             low+=1

#         elif num[mid]==1:
#             mid+=1

#         else :
#             Swap(mid,high,num)
#             # num[mid],num[high]=num[mid],num[high]
#             high-=1

#     return num

# def Swap(a,b,num):
#     temp=num[a]
#     num[a]=num[b]
#     num[b]=temp

#     return num


# num=[0,2,1,2,1,1,0,0,2]
# # print(f"DNF form : {DNF(num)}.")
# print(DNF(num))

"""
Moore's ALgorithm 
"""

# def Find(arr):
#     arr.sort()
#     majority=arr[0]
#     count=0

#     for i in arr:
#         if count==0:
#             majority=i
#             count=1

#         elif majority==i:
#             count+=1

#         else:
#             count-=1

#     vote=0
        
#     for i in arr :
#         if majority==i:
#             vote+=1

#     if vote>len(arr)/2:
#         return majority , vote
    
#     else:
#         return -1


# arr=[1,3,3,1,3,3,2]
# print(Find(arr))


"""
Move All Zeroes to End
"""

# arr=[1, 2, 0, 4, 3, 0, 5, 0]
# arr=[1,0,2,0,5]
# # arr=[10, 20, 30]
# # arr=[0, 2, 1, 0, 3, 0, 4, 0]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[j]==0:
#             temp=arr[i]
#             arr[i]=arr[j]
#             arr[j]=temp

#     print(arr)

#     print("-----------------")
# if 0 not in arr:
#     print("Zero is not exist.")
    
# print(arr)


"""
Moves Zeros to end without Brute force.
"""

arr=[0,1,2,0,5]

count=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[i],arr[count]=arr[count],arr[i]
        count+=1


print(arr)