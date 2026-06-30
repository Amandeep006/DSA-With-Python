"""BINARY SEARCH """

# This binary search is doing with the use of brute force.
# list=[]
# found=0
# n=int(input("Enter the Size of element :"))
# for i in range(n):
#     num=int(input("Enter the elements: "))
#     list.append(num)

# list.sort()
# print(list)
# target=int(input("Enter your target value :"))
# for i in list:
#     if i==target:
#         found=1
#         break
# if found==1:
#     print("The element is founded")
# else:
#     print("The element is not founded.")

# The time complexity =O(n) and space complexity = O(n)



""" So, We are improving the time complexity of the binary search with some techniques."""
list=[]
n=int(input("Enter the Size of element :"))
for i in range(n):
    num=int(input("Enter the elements: "))
    list.append(num)

list.sort()
print(f"List: {list}")
target=int(input("Enter your target value :"))

low=0
high=len(list)-1
mid=(low+high)//2
found=False
while True:
    mid=(low+high)//2
    if (list[mid]==target):
        print("The element is found")      
        break
    elif(list[mid]>target):
        high=mid
    else:
        if (list[mid]<target):
            low=mid
        else:
            break

# So the time complexity =O(n log n)