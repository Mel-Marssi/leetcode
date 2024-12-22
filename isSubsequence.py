class Solution(object):
	def isSubsequence(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if(s == ""):
			return True
		i = j = 0
		for i in range(len(t)):
			if(j in range(len(s)) and t[i] == s[j]):
				j += 1
			if(j == len(s)):
				return True
		return False

s = "abc"
t = "werqadefbhhhhhhdcee"
print(Solution().isSubsequence(s, t));