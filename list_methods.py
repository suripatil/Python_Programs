#!/usr/bin/python

lst = []
n = int(raw_input())
#Loop till all the commands are read
for i in range(0,n):
	read = raw_input()
	cmd = read.split()
	#check for the commands and perform the action
	if (cmd[0] == 'insert'):
		lst.insert(int(cmd[1]),int(cmd[2])) #pos,elem
	elif(cmd[0] == 'print'):
		print lst
	elif(cmd[0] == 'remove'):
		lst.remove(int(cmd[1]))
	elif(cmd[0] == 'append'):
		lst.append(int(cmd[1]))
	elif(cmd[0] == 'sort'):
		lst.sort()
	elif(cmd[0] == 'pop'):
		lst.pop()
	elif(cmd[0] == 'reverse'):
		lst.reverse()
	elif(cmd[0] == 'count'):
		lst.count(int(cmd[1]))
	elif(cmd[0] == 'index'):
		lst.index(int(cmd[1]))
	
		
	

