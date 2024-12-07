from typing import List

class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		for value in nums:
			print(value)
		return True

def __main__():
	list = [1, 2, 3, 4, 5, 6]
	solution = Solution()
	solution.containsDuplicate(list)

__main__()
