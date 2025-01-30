class Solution(object):
	def findDifference(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[List[int]]
		"""
		distinct1= []
		distinct2= []
		for i in range(len(nums1)):
			try:
				nums2.index(nums1[i])
			except ValueError:
				print(distinct1.count(nums1[i]))
				if(distinct1.count(nums1[i]) == 0):
					distinct1.append(nums1[i])
		for i in range(len(nums2)):
			try:
				nums1.index(nums2[i])
			except ValueError:
				if(distinct2.count(nums2[i]) == 0):
					distinct2.append(nums2[i])
		result = [distinct1, distinct2]
		return result


nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(Solution().findDifference(nums1, nums2))