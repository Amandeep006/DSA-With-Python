"""Insertion Sort of Python Implementation."""
list=[]
n=int(input("Enter the size of array :"))
for i in range(n):
    num=int(input(f"Enter the element{i+1}: "))
    list.append(num)

print(f"Before Swapping :{list}")

for i in range(1,n):
    key=list[i]
    j=i-1

    while j>=0 and list[j]>key:
        list[j+1]=list[j]
        j-=1

    list[j+1]=key
    print(list)
    print("--------------")


print(f"Before swapping : {list}")

# Time complexity : O(n^2) and Space Complexity : O(n)
