class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            target_diff = target - n
            if target_diff in seen:
                return [seen[target_diff],i]
            else:
                seen[n] = i

        



