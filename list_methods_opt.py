n = input()
l = []

for _ in range(n):
	read = raw_input().split()
	cmd = read[0]
	args = read[1:]
	
	if cmd !="print":
		cmd += "(" + ",".join(args) + ")"
		eval("l."+cmd)
	else:
		print l
