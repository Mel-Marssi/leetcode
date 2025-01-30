class Solution(object):
	def pivotIndex(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# left = right = sum(nums)
		for i in range(len(nums)):
			left = sum(nums[:i])
			right =sum(nums[i+1:])
			if( right == left):
				return i
		return(-1)
		
nums = [2,1,-1]
print(Solution().pivotIndex(nums))