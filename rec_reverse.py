#!/usr/bin/python3

#Recursively Reverse a string

def rec_rev(name):
	if(len(name) == 1):
		return name[0]
	else:
		return  rec_rev(name[1:]) + name[0]

print(rec_rev(['S','u','r','i']))
