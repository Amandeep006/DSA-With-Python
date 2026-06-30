"""Bubble Sorting is algorithm which used to sort the your array in the ascending or descending order."""

list=[]
n=int(input("Enter the Size of element :"))
for i in range(n):
    num=int(input("Enter the elements: "))
    list.append(num)

print(f"Before Sorting : {list}")

n=len(list)
for i in range(n-1):
    for j in range(n-i-1):
        if(list[j]>list[j+1]):
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp

print(f"After Sorting : {list}")

# Time complexity O(n^2 ) and Space Complexity O(n)