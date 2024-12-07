from typing import List

class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		seen = set()
		for num in nums:
			if num in seen:
				return True
			seen.add(num)
		return False

def __main__():
	list_1 = [1, 2, 3, 4, 5, 6]
	solution = Solution()
	print(solution.containsDuplicate(list_1))
	list_2 = [1, 2, 3, 4, 5, 6, 6]
	print(solution.containsDuplicate(list_2))

__main__()
