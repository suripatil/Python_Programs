#!/usr/bin/python3

def toString(List):
	return ' '.join(List)
def permute(a,l,r):
	if(l == r):
		print(toString(a))
	else:
		for i in range(l,r+1):
			a[l],a[i] = a[i],a[l]
			permute(a,l+1,r)
			a[l],a[i] = a[i],a[l]
st = "ABCD"
permute(list(st),0,len(st)-1)

