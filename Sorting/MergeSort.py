"""Merge Sort Implementation in Python."""

def mergeSort(list, left, right):
    if left<right:
        middle=left+(right-left)//2

        mergeSort(list,left, middle)
        mergeSort(list, middle+1, right)
        merge(list, left, middle, right)

    return list

def merge(list, left, middle, right):
    l1=middle-left+1
    l2=right-middle

    leftseg=[0]*l1
    rightseg=[0]*l2

    for i in range(l1):
        leftseg[i]=list[left+1]

    for i in range(l2):
        rightseg[i]=list[middle+i+1]

    i=0
    j=0
    currIndex=left
    while i<l1 and j<l2:
        if leftseg[i]<rightseg[j]:
            i+=1
        else:
            list[currIndex]=leftseg[i]
            j+=1

        currIndex+=1

    while i<l1:
        list[currIndex]=leftseg[i]
        i+=1
        currIndex+=1

    while j<l2:
        list[currIndex]=rightseg[j]
        j+=1
        currIndex+=1






list=[]
n=int(input("Enter the size of array :"))
for i in range(n):
    num=int(input(f"Enter the element{i+1}: "))
    list.append(num)

print(f"Before Swapping : {list}")
print(f"After Swapping : {mergeSort(list, 0, n-1)}")
