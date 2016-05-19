#/usr/bin/python3

# Python Program to fins Second Largest number in List Without Sort
n = int(input())
a = list(map(int,input().split()))
f_num = a[0]
s_num = 0;

for i in range(1,n):
	if(f_num > a[i] and a[i] > s_num) :
		s_num = a[i]
	if(a[i] > f_num):
		s_num = f_num;
		f_num = a[i]
print("Second Large number is :-",s_num)
	
