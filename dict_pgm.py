#!/usr/bin/python
from __future__ import division
import sys

dct = {};
#get n - number of students
n = int(raw_input());
if ( n >= 2) and (n <= 10) :
	for i in range(0,n):
		#read student details
		info = raw_input()
		new_info = info.split()
		name = new_info[0]
		del new_info[0]
		dct[name] = []

		for j in range(0,3):
			marks = float(new_info[j])					
			if ((marks >= float(0)) and (marks <= float(100))):
				dct[name].append(marks) 
			else:
				print("invalid marks for one of the student - >=0 and <= 100")	
				sys.exit(0)	
	print "dictionary details :- %s" % str(dct)
	#retrive student details
	info = raw_input()
	marks = 0
	if (info in dct):
		for j in dct[info]:
			marks += j

		print format(marks/3,'.2f')
	else:
		print("Student not found")

else:
	print("invalid n value - n >= 2 and n <= 10")
	sys.exit(0)
   


