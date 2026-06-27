"""Rotate the elements of the arr with the given rotation."""

from math import gcd
 
def rotate(arr,d):
    n=len(arr)
    gcdval=gcd(n,d%n)


    for i in range(gcdval):
        temp=arr[i]
        j=i
        while True:
            k=(j-d)%n 
            if k==i:
                break


            arr[j]=arr[k]
            j=k

        arr[j]=temp

    return arr


arr=[1,2,3,4,5]
print(rotate(arr,2))

# if use use - in k=j-d then it rotate right and otherwise it rotates in left direciton.
