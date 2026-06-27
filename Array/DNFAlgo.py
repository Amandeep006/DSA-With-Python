""" DNF (Dutch National FLag ) : it is sorthing technique designed to sort the 0's, 1's and 2's."""

def DNFAlgo(arr):
    n=len(arr)
    low=0
    mid=0
    high=n-1

    while mid<=high:
        if arr[mid]==0:
            swap(mid, low,arr)
            mid+=1
            low+=1

        elif arr[mid]==1:
            mid+=1
        
        else: 
            swap(mid,high,arr)
            high-=1

    return arr

def swap(a,b,arr):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp

    return arr
    
# Taking the user input 
arr=[]
pmt="\nIf you want to quit the loop, Just enter 'q "
pmt+="\nEnter the size of arr :"

while True:
    n=input(pmt)
    if n=='q':
        break
    print("Enter the elements :",end=" ")
    n=int(n)
    for i in range(n):
        num=int(input())
        arr.append(num)

    print(f"Sorting array : {DNFAlgo(arr)}.")  



      

