

#This function rotate the list by x number
def rotate(lst,x):
    copy = list(lst)
    for i in range(len(lst)):
        if x<0:
            lst[i+x] = copy[i]
        else:
            lst[i] = copy[i-x]

#Taking user input for 3 keys as k,l,m
k,l,m = input().split()
k=int(k)
l=int(l)
m=int(m)
#Taking input in str variable
str=input()

#Dividing all alphabets and _ in 3 groups in a list
t1=['a','b','c','d','e','f','g','h','i']
t2=['j','k','l','m','n','o','p','q','r']
t3=['s','t','u','v','w','x','y','z','_']

#initalizing list to store key value pair 
a1=[]
a2=[]
a3=[]

#enumerate through each element of str and
#if it matches to corresponding group,add it to that list.
for i,j in enumerate(str,0):
	if j in t1:
		a1.append(j)
		
	elif j in t2:
		a2.append(j)
		
	else:
		a3.append(j)


#Calling function to rotate all 3 lists
rotate(a1,k)
rotate(a2,l)
rotate(a3,m)

#initalizing variables
g=0
res=[]
p,q,r=0,0,0
#enumerate through str to check 
#which group this element belongs to
for i,j in enumerate(str,0):	
	if j in t1:
		res.append(a1[p])
		p+=1
	elif j in t2:
		res.append(a2[q])
		q+=1
	else:
		res.append(a3[r])
		r+=1

#Printing Result
for c in res:
	print(c,end="")
print()