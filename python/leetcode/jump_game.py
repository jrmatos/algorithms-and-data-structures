"""
Runtime
Details
405ms
Beats 77.19%of users with Python3
Memory
Details
17.48MB
Beats 90.03%of users with Python3
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        extra_steps = 1
        end = len(nums) - 1

        for i in range(len(nums)):
            if i == end:
                return True
            
            curr = nums[i]
            extra_steps -= 1

            if curr == 0 and extra_steps == 0:
                return False
            
            if curr > extra_steps:
                extra_steps = curr

"""
Better solution going backwards.

Runtime
Details
389ms
Beats 94.37%of users with Python3
Memory
Details
17.42MB
Beats 90.03%of users with Python3
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_good_index = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_good_index:
                last_good_index = i

        return last_good_index == 0
"""

