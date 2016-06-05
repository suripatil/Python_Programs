#!/usr/bin/python3 -tt

#Implementation of Insertion Sort Algorithm

def insertion_sort(a,n):
	for i in range(1,n):
		key = a[i]
		j = i - 1
		while (j >= 0 and key < a[j]):
			a[j+1] = a[j]
			j = j - 1
		a[j+1] = key
#Driver Program
a = [31,41,59,26,41,58]
print("Before Sort:-",a)
insertion_sort(a,6)
print("After Sort :-",a)
