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
num=[1,3,5,7,9]
sum=0
cum_sum=[]
for i in num:
    sum+=i
    cum_sum.append(sum)

print(f"Cumulative Sum: {cum_sum}")

