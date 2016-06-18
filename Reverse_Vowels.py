#!/usr/bin/python3
import sys
import re

#Optimized
def reverseVowels(s):
	#Ignore case and find 0 or 1 occurence of aeiou in s
	vowels = re.findall('(?i)[aeiou]',s)
	print("Vowels Found:",vowels)
	return re.sub('(?i)[aeiou]',lambda m:vowels.pop(),s)

#Brute Force
def reverse_vowels(s):
 vowels = ['a','e','i','o','u','A','E','I','O','U']
 i = 0
 j = len(s)-1
 while(i < j):
  if(s[i] not in vowels):
   i += 1
  if(s[j] not in vowels):
   j -= 1
  if(s[i] in vowels and s[j] in vowels):
   s[i],s[j] = s[j],s[i]
   i += 1
   j -= 1
 return ''.join(s)

	
if __name__ == "__main__":
	s = sys.argv[1]
	print("Before Reverse:",s)
	print("After Reversing vowels:",reverseVowels(s))
		
