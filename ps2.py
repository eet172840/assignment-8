###### this is the second .py file ###########

#Taking keys as input which are space separated
k,l,m = input().split()
k=int(k)
l=int(l)
m=int(m)
#taking input string which is encrypted
str=input()


#storing all 26 words and _ in tuple to divide in 3 groups
t1=('a','b','c','d','e','f','g','h','i')
t2=('j','k','l','m','n','o','p','q','r')
t3=('s','t','u','v','w','x','y','z','_')

#initalizing dictionary to store key value pair 
a1={}
a2={}
a3={}
for i,j in enumerate(str,0):
	if j in t1:
		a1[i]=j
		
	elif j in t2:
		a2[i]=j
	else:
		a3[i]=j

print(a1)
print(a2)
print(a3)