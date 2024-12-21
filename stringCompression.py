class Solution(object):
	def compress(self, chars):
		"""
		:type chars: List[str]
		:rtype: int
		"""
		tmp = chars[0]
		count = 0
		result = ""
		for i in chars:
			if(tmp != i):
				result += tmp
				if(count > 1):
					result+=(str(count))
				tmp = i
				count = 0
			count+=1
		if count > 0:
			result += (tmp)
			if(count > 1):
				result += (str(count))
		# chars.clear()
		for i in range(len(chars)):
			if(i < len(result)):
				chars[i] = (result[i])
			else:
				chars.pop()
		
		return len(result)
				
chars =["a","a","b","b","c","c","c"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(Solution().compress(chars))
print(chars) # ["a","2","b","2","c","3"]