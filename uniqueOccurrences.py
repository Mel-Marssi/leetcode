class Solution(object):
	def uniqueOccurrences(self, arr):
		"""
		:type arr: List[int]
		:rtype: bool
		"""
		hashMap = {}
		for i in range(len(arr)):
			if(arr[i] not in hashMap):
				hashMap[arr[i]] = 1
			else:
				hashMap[arr[i]] += 1
		if(len(hashMap.values()) !=  len(set(hashMap.values()))):
				return False
		return True

arr = [1,2,2,1,1,3]
print(Solution().uniqueOccurrences(arr))