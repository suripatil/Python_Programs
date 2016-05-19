#!/usr/bin/python

#Python Program to implement the Functionality of Python Signly list 

class Node(object):
	def __init__(self,data):
		self.val = data
		self.nextn = None

class List(object):
	
	def __init__(self):
		self.head = None
		self.size = 0

	def IsEmpty(self):
		return self.size == 0

	def Insert(self,data):
		n = Node(data)
		n.nextn = self.head
		self.head = n
		self.size += 1
	
	def Delete(self,data):
		if self.IsEmpty():
			print("List Empty")
			return
		temp = self.head
		while temp:
			if(temp.val == data) and (temp.nextn is not None):
				temp.val = temp.nextn.val
				temp.nextn = temp.nextn.nextn
			temp = temp.nextn
	def Display(self):
	 	temp = self.head
		while temp:
			print temp.val,"->",
			temp = temp.nextn
		print ""

#Main Driver Program
if __name__ == "__main__":
	first = List()
	
	#insert Elements
	first.Insert(10)
	first.Insert(20)
	first.Insert(30)
	first.Insert(40)

	#display list
	first.Display()

	#Remove 20 and Display List
	first.Delete(10)
	first.Display()

	


	
	
