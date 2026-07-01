""""Selection Sort Algorithm implementation."""
list=[]
n=int(input("Enter the size of element :"))
for i in range(n):
    num=int(input("Enter the elements: "))
    list.append(num)

print(f"Before Sorting : {list}")

for i in range(n):
    mintext=i
    for j in range(i,n):
        if list[mintext]>list[j]:
            mintext=j
        

    temp=list[i]
    list[i]=list[mintext]
    list[mintext]=temp


print(f"After Swapping : {list}")