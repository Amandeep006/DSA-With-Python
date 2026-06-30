"""Time Complexity : Time complexity tells us how the number of operations increases the input size."""

# it does mean : How many seconds, It means : How many operations
print("Hello") # time complexity= O(1)

"""LINEAR TIME"""

for i in range(n):
    print(i)
# suppose n=5 then its time complexity becomes O(n) because n=5


for i in range(n):
    for j in range(n):
        print(i,j)
# Suppose n=3, run =9 times then its time complexity becomes O(n^2)


for i in range(n):
    for j in range(10):
        print(i,j)
# Suppose n=3, but its time complexity becomes O(n) instead of O(10n) because  in the complexity, we ignore the  constant values. it also have a reason why we ignore the constant because Big-O focus on the growth rate, not the exact number of operations.


for i in range(n):
    print(i)

for i in range(n):
    print(j)
# Suppose n=3 then its time complexity becomes O(n) instead of O(n+n)=O(2n)


for i in range(n):
    print(i)

for j in range(n*n):
    print(j)
# Operations n+n^2 then its time complexity becomes O(n^2) instead of O(n+n^2)



"""LOGARITHMIC TIME O(log n)"""
while n>1:
    n=n//2
# Suppose n=16, SO iteration goes 4 So, that's time complexity becomes O(log n)


