"""Space Complexity : Space complexity tells us how much extra memory an algorithm uses.

Array size=space complexity # but it not mean space complexity.

input memory is usually not counted. Actually we mainely count he extra memory created by the algoeithm.
"""

sum=0
for i in arr:
    sum+=1
# Extra variable is "sum=i" that'why space complexity becomes O(1)


new=[]
for i in arr:
    new.append(i)
# suppose n=100, new arr size=100 then its space complexity O(100) or O(n)


matrix=[[0]*n for _ in range(n)]
# memory nxn and space O(n^2)


def fun(n):
    if n==0;
        return 
    
fun(n-1)
# Suppose fun(5) then total 6 stack frames and its space complexity becomes O(n).

"""Now both space and time complexity"""

for i in range(n):
    for j in range(i+1,n):
        pass

# Time complexity: O(n^2) and Space complexity : O(1)


visited={}

for x in arr:
    pass

# Time complexity : O(n) and Space complexity : O(n)


