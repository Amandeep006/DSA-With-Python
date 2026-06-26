""" Kadan's Algorithm is used to find the maximum sum of a contigious subarray in an array."""

"""1D Array"""
# list=[5,-2,3,-7,-6,11,-2,7,8,-14]
# maxSumTillNow=list[0]
# maxSumInCurrWindow=0

# for i in range(0,len(list)):
#     maxSumInCurrWindow= maxSumInCurrWindow + list[i]
#     if(maxSumInCurrWindow>maxSumTillNow):
#         maxSumTillNow=maxSumInCurrWindow
#     elif(maxSumInCurrWindow<0):
#         maxSumInCurrWindow=0

# print(f"The Maximum Sum of subarray : {maxSumTillNow}.")


"""2D array, find the maximum sum of rectangle. """
import sys

def kadaneAlgorthim(givenNums):
    start=0
    end=0

    currSum=0
    maxSum=-sys.maxsize -1

    n=len(givenNums)

    while end<n:
        while currSum<0:
            currSum-=givenNums[start]
            start+=1

        currSum+=givenNums[end]
        end+=1

        maxSum=max(maxSum,currSum)
    
    return maxSum


list=[[3,8,9,1,3],[-4,-1,1,7,-6],[-2,-3,8,1,-1]]

n=len(list) # Lenght of rows
m=len(list[0]) # Length of columns

ans=-sys.maxsize -1


for i in range(m):
    temp=[]
    for j in range(n):
        temp.append(list[j][i])

    print(temp)

    ans=max(ans, kadaneAlgorthim(temp))
    print(ans)


    for j in range(i+1,m):
        for k in range(n):
            temp[k]+=list[k][j]
        
        print(temp)

        ans=max(ans, kadaneAlgorthim(temp))

        print(ans)
    
    print("---------------------------")


print(ans)