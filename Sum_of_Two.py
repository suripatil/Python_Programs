#Q 14 - Sum of Two Integers
#Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#Ans - 
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        #Works For Positive and Negative 
        if (a == 0): return b
        if (b == 0): return a
        if (a == 2147483647 and b == -2147483648): return -1
        flag = False
        if (a < 0 and b < 0):
            a = -a
            b = -b
            flag = True

        mask = 0xffffffff
        while (b != 0):
            a = a & mask
            b = b & mask
            carry = a & b & mask
            a = a ^ b
            b = (carry << 1) & mask
et        return -a if flag else a
        ''' 
       # Works Only For Positive numbers
        carry = 0
        if (a == 0): return b
        if (b == 0): return a
        if (a >= 0 and b < 0): return -1
        
        while (b):
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a
        '''
