"""Using the Break statement."""
# limit=10
# cursum=0

# while True:
#     num=int(input())
#     if cursum+num>limit:
#         print(cursum,"limit reached")
#         break

#     cursum+=num


"""Pattern printing questions."""
# 1 2 3
# 1 2 3

# n=int(input("Enter number of rows:"))
# m=int(input("Enter number of column:"))

# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(j,end=" ")
#     print("\n")


# 1
# 12
# 123
# 1234

# n=int(input("Enter the size:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")

#     print("")


    
#     *
#    **
#   ***
#  ****
# ***** 


n=int(input("Enter the size:"))
for i in range (n,0,-1):
    for j in range (1,n+1):
        if(j<i):
            print(" ",end="")
        else:
            print("*",end="")
    print("")    
    


