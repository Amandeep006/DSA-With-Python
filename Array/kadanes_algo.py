""" Kadan's Algorithm is used to find the maximum sum of a contigious subarray in an array."""

"""1D Array"""
list=[5,-2,3,-7,-6,11,-2,7,8,-14]
maxSumTillNow=list[0]
maxSumInCurrWindow=0

for i in range(0,len(list)):
    maxSumInCurrWindow= maxSumInCurrWindow + list[i]
    if(maxSumInCurrWindow>maxSumTillNow):
        maxSumTillNow=maxSumInCurrWindow
    elif(maxSumInCurrWindow<0):
        maxSumInCurrWindow=0

print(f"The Maximum Sum of subarray : {maxSumTillNow}.")