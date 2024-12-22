class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		i = 0
		j = len(height) - 1
		area = 0
		while (j > i):
			distance = j - i
			if (height[i] > height[j]):
				L = height[j]
				j -= 1
			else:
				L = height[i]
				i += 1
			area = max(area, distance * L)
		return area


height =  [1,8,6,2,5,4,8,3,7] #7
print(Solution().maxArea(height))

