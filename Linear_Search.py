#/usr/bin/python3 -tt

#Implementation of Linear Search

def linear_search(a,n,v):
	for i in range(0,n):
		if(a[i] == v):
			return i
	return None

#Driver Program
a = [10,20,30,40,50]
print(linear_search(a,5,20))
