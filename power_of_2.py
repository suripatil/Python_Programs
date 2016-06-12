#231. Power of Two
#Given an integer, write a function to determine if it is a power of two.
#Solution :-
#Consider the Binary Representation for Below Number’s:
# 1 -> 00000001
# 2 -> 00000010

#N & N-1 will clear the rightmost bit set in number and perform & operation by subtracting 1 from N i.e. (n-1). Result is 0 if it is power of 2 , 1 otherwise.

#Python [Accepted] - Optimised and Faster Solution
class Solution(object):
    def isPowerOfTwo(self, n):
       if n <= 0:
            return False
        else:
            return n & (n-1) == 0


