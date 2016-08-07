#!/usr/bin/python3

#Program to valida the IP Address and Print the class of the IP
#Ex - 10.0.0.0 - 10.255.255.255 -Class A - NetId 8 Bits , Host Id 24 Bits
#   - 172.16.0.0 - 172.31.255.255 - Class B - NetID 12 Bits, Host ID 20 Bits
#   - 192.168.0.0 - 192.168.255.255 - Class C - NetID 16 Bits , Host ID 16 Bits
#   - 127.0.0.0 to 127.255.255.255 - LocalHost / LoopBack


'''
Steps -
	Read Input
	Validate IP
	split with input with . and Store in List
	parse list items form 1 to 4 with above Conditions
'''

import re

def validate_ip(ip_addr):

	if re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ip_addr):
	  lst = list(map(int,ip_addr.split('.')))
	  
	  #CLASS A Range - 10.0.0.0 - 10.255.255.255	
	  if((lst[0] == 10) and (lst[1] >= 10 and lst[1] <= 255) and (lst[2] >= 0 and lst[2] <= 255) 
	  	 and (lst[3] >= 0 and lst[3] <= 255)):
	    print("IP",ip_addr,"is Class A")
	  
	  #CLASS B Range - 172.16.0.0 - 172.31.255.255	
	  elif((lst[0] == 172) and (lst[1] >= 16 and lst[1] <= 31) and (lst[2] >= 0 and lst[2] <= 255) 
		and (lst[3] >= 0 and lst[3] <= 255)):
	    print("IP",ip_addr,"is Class B")
	
	  #CLASS C Range - 192.168.0.0 - 192.168.255.255	
	  elif((lst[0] == 192) and (lst[1] == 168) and (lst[2] >= 0 and lst[2] <= 255) 
		and (lst[3] >= 0 and lst[3] <= 255)):
	    print("IP",ip_addr,"is Class C")
	  
	  #Loop Back Range - 127.0.0.0 - 127.255.255.255	
	  elif((lst[0] == 127) and (lst[1] >= 0 and lst[1] <= 255) and (lst[2] >= 0 and lst[2] <= 255) 
		and (lst[3] >= 0 and lst[3] <= 255)):
	    print("IP",ip_addr,"is Loop Back Host Address")
	  else:
	    print("Invalid Private IP Address Range")		
	else:
	    print("Invalid Ip Adress String")

if __name__ == "__main__":
	ip_addr = input("Enter Ip Address :-")
	validate_ip(ip_addr)
