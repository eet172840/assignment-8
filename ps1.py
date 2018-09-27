###### this is the first .py file ###########

#importing array package from python library
from array import *
import copy

#This function checks for largest cross for each cell
def safe(a,x,y,m,n):
	count=1
	if a[x][y]=='D':
		return 0

	if m>3 and n>4:
		while x>0 and y>0 and x<m-1 and y<n-1 and a[x][y]=='S':
			if a[x+1][y]=='S' and a[x][y+1]=='S' and a[x-1][y]=='S' and a[x][y-1]=='S':
				x+=1
				y+=1
				count+=4
			else:
				a[x+1][y]=a[x][y+1]=a[x-1][y]=a[x][y-1]='D'
				break
	else:
		while x>0 and y>0 and x<m-1 and y<n-1 and a[x][y]=='S':
			if a[x+1][y]=='S' and a[x][y+1]=='S' and a[x-1][y]=='S' and a[x][y-1]=='S':
				a[x+1][y]=a[x][y+1]=a[x-1][y]=a[x][y-1]='D'
				x+=1
				y+=1
				count+=4

	return count
	
	
#taking input from user for dimensions of matrix
n,m = input().split()
n=int(n)
m=int(m)
#check boundary conditions
if n>150 or m>150:
	print("Out of range")
	print(exit)


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


#Initializing list
lst=[]
#This loop checks for safe sequence for each cell.
for i in range(n):
	count=1
	for j in range(m):
		count=safe(arr,i,j,n,m)
		#append result in list
		lst.append(count)

#Sort list in non increasing order
ans=sorted(lst,reverse=True)
#print result
print(ans[0],end=" ")
print(ans[1])





#initializing array to store values
'''
arr1=[[] for i in range(n)]
for j in range(m):
	arr1[j].append(input())

arr = copy.deepcopy(arr1)

'''