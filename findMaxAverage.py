class Solution(object):
	def findMaxAverage(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: float
		"""
		maxSub = tmpSub = sum(nums[:k])
		for i in range(len(nums) - k):
			tmpSub = tmpSub - nums[i] + nums[i+k]
			if(tmpSub > maxSub):
				maxSub = tmpSub
		return float(maxSub/k)

nums = [1,12,-5,-6,50,3]
k = 4
print(Solution().findMaxAverage(nums, k))