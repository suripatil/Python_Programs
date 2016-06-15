#!/usr/bin/python

#Given an integer, write a function to determine if it is a power of three.
#Follow up:
#Could you do it without using any loop / recursion?

#Solution 1 - (Only to find power of 3)
def power_of_3(n):
	return n>0 == 3 **19 % n

#Solution 2 - Brute Force
def power_of_n(n,num):
	while (num % n == 0):
		num = num // n
	return num == 1
	 
if __name__ == "__main__":
	n = 4
	num = 16
	if(power_of_n(n,num) == True):
		print(num,"is power of",n)
	else:
		print(num,"is not power of ", n) 
