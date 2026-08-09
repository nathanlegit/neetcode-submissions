class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicate = False
        my_set = set()
        for i in range(len(nums)):
            if nums[i] in my_set:
                has_duplicate = True
            else:
                my_set.add(nums[i])
        return has_duplicate

           