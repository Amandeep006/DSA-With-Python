"""Here we also solve some other algorithm which comes in the array topic."""

"""
1. we have N length of array (1--n). SO, a) We only repeat 1 element occur in twice. b) and 1 element is not present in the array (missing).
"""

def solve(givenNums):
    repeating=-1
    missing=-1
    currsum=0
    totalSum=(len(givenNums)*(len(givenNums)+1))//2

    for i in range(len(givenNums)):
        if givenNums[abs(givenNums[i]-1)]<0:
            repeating=abs(givenNums[i])
        givenNums[abs(givenNums[i])-1] *=-1

        currsum +=abs(givenNums[i])

    missing=totalSum-(currsum-repeating)
    print(f"Repeating : {repeating}, Missing : {missing}")

givenNums=[1,2,3,1,5]
solve(givenNums)


"""
2. We have also an array of N. SO, 
a. we have only single element whose repeat.
b. NO change to given array.
c. We have a constant space.

"""

def findrepeating(givenNums):
    slow=givenNums[0]
    fast=givenNums[givenNums[0]]

    while slow!=fast:
        slow=givenNums[slow]
        fast=givenNums[givenNums[fast]]

    slow=0

    while slow!=fast:
        slow=givenNums[slow]
        fast=givenNums[fast]

    return slow


givenNums=[1,2,3,5,1,1]
print(findrepeating(givenNums))