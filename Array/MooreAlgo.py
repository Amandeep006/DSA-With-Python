"""Find the majority element in the given array."""

"""Firstly solve this problem using the brute force technique."""

# arr=[1,2,3,3,1,2,3]
# count=0

# for i in arr:
#     for j in arr:
#         if i==j:
#             num=j
#             count+=count

# print(num)

# But the brute force technique take time complexit O(n^2) and space complexity O(n), That's why we use the Morre's Voting algorthim has take time complexity O(n) and space complexity O(1).


"""Moore's Voting Algorithm"""
def find_majority_element(arr):
    candidate = None
    count = 0
    
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
            
    actual_count = 0
    for num in arr:
        if num == candidate:
            actual_count += 1
            
    if actual_count > len(arr) // 2:
        return f" Candidate : {candidate}, Actual_count : {actual_count} "
    else:
        return "No Majority Element Found"


nums = [1,3,1,2,8]
print("Majority Element:", find_majority_element(nums))


