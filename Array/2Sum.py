""" We are using a 2Sum method to find the targeted value."""

# def solve(givenNums, Target):
#     givenNums.sort()
#     start=0
#     end=len(givenNums)-1

#     while start<end:
#         currsum=givenNums[start] + givenNums[end]
#         if currsum==Target:
#             return [givenNums[start], givenNums[end]]
        
#         if currsum>Target:
#             end-=1
#         else:
#             start+=1

#     return -1

# givenNums=[1,5,2,10,7]
# target=17
# givenNums.sort()
# print(givenNums)

# print(f"The 2Sum of the list :{solve(givenNums,target)}")

""" We are using a #Sum method to find the target value and return 3 values."""

def solve(givenNums, Target):
    temp=givenNums.copy()
    givenNums.sort()

    for k in range(len(givenNums)):
        temptarget=Target
        temptarget-=givenNums[k]
        start=k+1
        end=len(givenNums)-1

        while start<end:
            currsum=givenNums[start] + givenNums[end]
            if currsum==temptarget:
                ans=[]

                for i in range(len(temp)):
                    if givenNums[start]==temp[i] or givenNums[end]==temp[i] or givenNums[k]==temp[i]:
                        ans.append(i)
                
                return ans              
            
            if currsum>Target:
                end-=1
            else:
                start+=1

        return -1

givenNums=[1,5,2,10,7]
target=8

print(solve(givenNums,target))

        