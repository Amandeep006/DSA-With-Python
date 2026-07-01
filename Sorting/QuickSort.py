""" Quick Sort Implementation in Python. """

def quickSort(list, low, high):
    if low<high:
        pi=partition(list,low,high)

        quickSort(list,low,pi-1)
        quickSort(list,pi+1,high)

    return list

def partition(list,low,high):
    pivot=list[high]
    i=low-1

    for j in range(low,high):
        if list[j]<pivot:
            i+=1
            list[i],list[j]=list[j],list[i]

    list[i+1], list[high]=list[high], list[i+1]

    return i+1


list=[]
n=int(input("Enter the size of array :"))
for i in range(n):
    num=int(input(f"Enter the element{i+1}: "))
    list.append(num)

print(f"Before Swapping : {list}")
print(f"After Swapping : {quickSort(list,0,len(list)-1)}")

