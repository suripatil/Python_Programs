#!/usr/bin/python3

#Python Program to Print Directory and Files Recursively

import os

def print_dir(path):
	for dirName,subdirList,fileList in os.walk(path):
		print("--- Directory ---",str(dirName))
		for fl in fileList:
			print("\t",str(fl))


if __name__ == "__main__":
	path = input("Enter the directory path :-")
	print_dir(path)

		
	
