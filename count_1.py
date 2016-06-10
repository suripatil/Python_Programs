def hammingWeight(n):
	"""
        :type n: int

        :rtype: int

        """
	count = 0
	while(n):
		count += 1
		n &= (n-1)
	print(count)

hammingWeight(11)
