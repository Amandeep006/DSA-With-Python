""" Kadan's Algorithm is used to find the maximum sum of a contigious subarray in an array."""

"""1D Array"""
# list=[5,-2,3,-7,-6,11,-2,7,8,-14]
# maxSumTillNow=list[0]
# maxSumInCurrWindow=0

# for i in range(0,len(list)):
#     maxSumInCurrWindow= maxSumInCurrWindow + list[i]
#     if(maxSumInCurrWindow>maxSumTillNow):
#         maxSumTillNow=maxSumInCurrWindow
#     elif(maxSumInCurrWindow<0):
#         maxSumInCurrWindow=0

# print(f"The Maximum Sum of subarray : {maxSumTillNow}.")


"""2D array, find the maximum sum of rectangle. """
list=[[-3,8,9,1,3],[-4,-1,1,7,-6],[-2,-3,8,1,-1]]
maxnumsum=[]
maxretsum=0
maxretleft=0
maxretright=0
maxrettop=0
maxretbottom=0

n=len(list) # Lenght of rows
m=len(list[0]) # Length of columns

# for i in range(n):
#     for j in range(m):
#         print(list[i][j],end=" ")
#     print("")

print("----------------------------")

# for i in range(n):
#     for j in range()
#     for j in range(m):

for i in range(n):
    for j in range(m):
        print(list[i][j] )