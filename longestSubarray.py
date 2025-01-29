class Solution(object):
	def longestSubarray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		start, trackZero , tmpMax = 0,0,0
		zeroFlag = 0
		for start in range(len(nums)):
			if(nums[start] == 0):
				zeroFlag += 1
			while(zeroFlag == 2):
				if(nums[trackZero]== 0):
					zeroFlag -= 1
				trackZero += 1
			tmpMax = max(tmpMax, start - trackZero)
		return tmpMax



		# end = tmpMax = 0
		# zeroFlag = 0
		# for start in range(len(nums)):
		# 	if(nums[start] == 0):
		# 		zeroFlag += 1
		# 	while(zeroFlag > 1):
		# 		if(nums[end] == 0):
		# 			zeroFlag -= 1
		# 		end += 1
		# 		print(start, end)
		# 	tmpMax = max(tmpMax, start - end)
		# 	print(tmpMax, " ---> ", start, end)
		# return tmpMax



nums = [0,1,1,1,0,1,1,0,1]
print(Solution().longestSubarray(nums))