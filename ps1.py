###### this is the first .py file ###########

#importing array package from python library
from array import *



def safe(a,x,y,m,n):
	count=1
	if x>0 and y>0 and x<m-1 and y<n-1 and a[x][y]=='1':
		if a[x+1][y]=='1' and a[x][y+1]=='1' and a[x-1][y]=='1' and a[x][y-1]=='1':
			a[x+1][y]=a[x][y+1]=a[x-1][y]=a[x][y-1]='0'
			
			if x+1>0 and y+1>0 and x<m-2 and y<n-2:
				if a[x+2][y]=='1' and a[x][y+2]=='1' and a[x-2][y]=='1' and a[x][y-2]=='1':
					return count+8;

			return count+4;
	if a[x][y]=='0':
		return 0;
	return 1;


#taking input from user for dimensions of matrix

n,m = input().split()
n=int(n)
m=int(m)
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
'''
arr2=[]
for r in arr:
    for c in r:
    	
        print(c,end = "")
    print()

'''


for i in range(n):
    for j in range(m):
    	if arr[i][j]=='S':
    		arr[i][j]='1'
    	else:
    		arr[i][j]='0'
        #print(arr[i],end = "")
    print()

for r in arr:
    for c in r:
    	print(c,end = "")
	
lst=[]
for i in range(n):
	count=1
	for j in range(m):
		count=safe(arr,i,j,n,m)
		lst.append(count)

print(count)
print(lst)
ans=sorted(lst,reverse=True)
print(ans[0],end=" ")
print(ans[1])

'''
#print(arr)
print()
lst=[]
count=0

for i in range(n):
	 count=1
	 for j in range(m):
	 	if i>0 and j>0 and i<n-1 and j<m-1 and arr[i][j]=='1':
	 		if arr[i][j-1]=='1' and arr[i][j+1]=='1' and arr[i+1][j]=='1' and arr[i-1][j]=='1':
	 			count=5
	 			if i-2>=0 and j-2>=0 and i+2<=n-1 and j+2<=m-1:
	 				if arr[i][j-2]=='1' and arr[i][j+2]=='1' and arr[i+2][j]=='1' and arr[i-2][j]=='1':
	 					count=9

	 lst.append(count)
				

			
    			#lst.append(count)
    			#print(count)


    					

    					
    					

    
	
sorted(lst)	
    					#if arr[i][j-2]=='1' and arr[i-2][j-2]=='1' and arr[i][j+2]=='1' and arr[i+2][j+2]=='1':
print(lst) 					#	count+=4

    	
#print(count)
print(lst[1],end=" ")
print(lst[0])
'''