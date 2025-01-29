class Solution(object):
	def largestAltitude(self, gain):
		"""
		:type gain: List[int]
		:rtype: int
		"""
		tmpMax = gain[0]
		sumt = gain[0]
		for i in range(len(gain)):
			if(i + 1 in range(len(gain))):
				sumt +=  gain[i+1]
				tmpMax =  max(tmpMax, sumt )
				print(sumt)
		tmpMax = max(0, tmpMax)
		return tmpMax

gain = [52,-91,72]
print(Solution().largestAltitude(gain))