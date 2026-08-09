class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate 'a' values
            left_index = i + 1
            right_index = len(nums) - 1
            target = -nums[i]
            while left_index < right_index:
                guess = nums[left_index] + nums[right_index]
                if guess == target:
                    results.append([nums[i], nums[left_index], nums[right_index]])
                    left_index += 1
                    right_index -= 1
                    while left_index < right_index and nums[left_index] == nums[left_index - 1]:
                        left_index += 1  # skip duplicate 'b' values
                elif guess < target:
                    left_index += 1
                else:
                    right_index -= 1
        return results