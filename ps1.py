###### this is the first .py file ###########

#importing array package from python library
from array import *

#taking input from user for dimensions of matrix
n=int(input())
m=int(input())

#initializing array to store values
arr = []
for i in range(n):
    arr.append([])
    for j in range(m):
    	#appending either D or S in array
        arr[i].append(input())


#This loop is printing input taken in desired format
for r in arr:
    for c in r:
        print(c,end = "")
    print()

#Now searching for pattern