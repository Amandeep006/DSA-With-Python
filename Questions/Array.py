"""
Given an integral array nums, return the number of reverse pairs in the array.
a reverse pair is a pair (i,j).
 Where :
* 0<=i<j<nums.length and 
* nums[i]>2>nums[j].
"""

# Firstly apply the brute force.
def solve(nums):
    count=0
    n=len(nums)
    for i in range(n):
        for j in range(1,n):
            if(i<j):
                if(nums[i]>2*nums[j]):
                    count+=1
                    print(f"Reverse pair : ({i},{j})")                        
            
    print(f"The total count of the pairs : {count}.")       
   
                
nums=[1,3,2,3,1]
solve(nums)