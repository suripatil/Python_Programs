#!/usr/bin/python3

#Python Program to Print Directory and Files Recursively

import os

def print_dir(path):
	for dirName,subdirList,fileList in os.walk(path):
		nw_path = dirName.split('/')
		print("|",(len(nw_path))*"---","[",os.path.basename(dirName),"]")
		for fl in fileList:
			print("|",len(nw_path)*"---","->",str(fl))


if __name__ == "__main__":
	path = input("Enter the directory path :-")
	print_dir(path)

		
	
