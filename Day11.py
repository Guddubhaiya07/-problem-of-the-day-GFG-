#Palindrome 
class Solution:
	def isPalinSent(self, s):
		# code here
		s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]
